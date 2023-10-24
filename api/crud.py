import asyncio
from time import time_ns

from sqlalchemy import func, select, text, update
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.orm import Session

from .database import engine
from .models import Item
from .utils import filter_data, get_data_json


def get_oldest_item_id(only_listed: bool = False):
    with Session(engine) as session:
        if only_listed:
            oldest_item = (
                session.query(Item)
                .filter(Item.is_listed == True)
                .order_by(Item.updated_at, Item.alphabetical_order)
                .first()
            )
        else:
            oldest_item = (
                session.query(Item)
                .order_by(Item.updated_at, Item.alphabetical_order)
                .first()
            )
    print(oldest_item.full_name.encode("utf-8"))
    return oldest_item


def get_item_by_full_name(full_name: str):
    with Session(engine) as session:
        item = session.query(Item).filter(Item.full_name == full_name).first()
    return item


def get_items_by_range_alphabetical_order(start: int, end: int):
    with Session(engine) as session:
        items = (
            session.query(Item)
            .filter(Item.alphabetical_order >= start, Item.alphabetical_order <= end)
            .all()
        )
    return items


def set_item_listing(full_name: str, is_listed: bool = False):
    with Session(engine) as session:
        item = session.query(Item).filter(Item.full_name == full_name).first()
        item.is_listed = is_listed
        session.commit()
    return


async def add_item_data(
    appid: int,
    last_item: int = 0,
    steam_total_count: int = 0,
    last_error: bool = False,
    building: bool = True,
    oldest_item_name: str = "",
):
    if building:
        with Session(engine) as session:
            start = session.query(Item).count()
            last_item = start
        print(start, steam_total_count)
        if start > steam_total_count != 0:
            building = False
            return last_item, steam_total_count, last_error, building, oldest_item_name
    elif last_error:
        start = last_item
    else:
        oldest_item = get_oldest_item_id(only_listed=True)
        start = oldest_item.alphabetical_order
        if not last_error and oldest_item_name == oldest_item.full_name:
            last_item -= 100
            start = last_item
        else:
            last_item = start

        oldest_item_name = oldest_item.full_name

    start = max(0, min(start, steam_total_count))

    print("Updating items from: " + str(start))

    time = time_ns()
    data = await get_data_json(appid, start=start, sort_column="name", sort_dir="asc")
    print(f"Got data in: {(time_ns() - time)/10**9} s")
    if not data:
        print("Error: request empty")
        last_error = True
        return last_item, steam_total_count, last_error, building, oldest_item_name

    steam_total_count = data["total_count"]

    if not data["results"]:
        print("Error: request results empty")
        last_error = True
        return last_item, steam_total_count, last_error, building, oldest_item_name

    last_error = False

    if len(data["results"]) < 100:
        print("Less than 100 results")
        building = False
        return last_item, steam_total_count, last_error, building, oldest_item_name

    filter_keys = ["name", "sell_listings", "sell_price", "icon_url", "appid"]

    time = time_ns()
    data_filtered = await filter_data(data, filter_keys)
    print(f"Filtered data in: {(time_ns() - time)/10**9} s")

    with Session(engine) as session:
        stmt = (
            insert(Item)
            .values(data_filtered)
            .on_conflict_do_update(
                index_elements=["full_name"],
                set_=dict(
                    sell_listings=insert(Item)
                    .values(data_filtered)
                    .excluded.sell_listings,
                    sell_price=insert(Item).values(data_filtered).excluded.sell_price,
                    updated_at=insert(Item).values(data_filtered).excluded.updated_at,
                    is_listed=True,
                ),
            )
        )
        session.execute(stmt)
        session.commit()
    set_item_alphabetical_order(only_listed=True)

    # check if item that should be in update range was updated if not set is_listed to false
    request_full_names = [item["full_name"] for item in data_filtered]
    database_full_names = get_items_by_range_alphabetical_order(
        get_item_by_full_name(request_full_names[0]).alphabetical_order,
        get_item_by_full_name(request_full_names[-1]).alphabetical_order,
    )

    for item in database_full_names:
        if item.full_name not in request_full_names:
            set_item_listing(item.full_name, False)

    return last_item, steam_total_count, last_error, building, oldest_item_name


def set_item_alphabetical_order(only_listed: bool = False):
    with Session(engine) as session:
        # update = text(
        #     f"""
        #     UPDATE items
        #     SET alphabetical_order = t.rn
        #     FROM (
        #         SELECT id, ROW_NUMBER() OVER (ORDER BY lower(full_name) collate "C") AS rn
        #         FROM items
        #         WHERE is_listed = {only_listed}
        #     ) t WHERE t.id = items.id
        #     """
        # )

        subquery = (
            select(
                Item.id,
                func.row_number()
                .over(order_by=func.lower(Item.full_name).collate("C"))
                .label("rn"),
            ).where(Item.is_listed == only_listed)
        ).alias("subquery")

        update_stmt = (
            update(Item)
            .values(alphabetical_order=subquery.c.rn)
            .where(subquery.c.id == Item.id)
        )
        # print(str(update_stmt))

        session.execute(update_stmt)
        session.commit()
    return "done"


def get_items(db: Session, limit: int = 100):
    items = db.query(Item).limit(limit).all()
    return items
