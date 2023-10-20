from sqlalchemy import func, select, text, update
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.orm import Session

from .database import engine
from .models import Item
from .utils import filter_data, get_data_json

# building = True
last_item = 0
last_error = False
# last_updated = True
steam_total_count = 0


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


# print(get_oldest_item_id().id)
# print("cos")


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


async def add_item_data(appid: int):
    global last_item, steam_total_count, last_error
    # global building, last_error, steam_total_count, last_updated, last_item
    # if building:
    #     with Session(engine) as session:
    #         start = session.query(Item).count()
    #         last_item = start
    # else:
    #     start = get_oldest_item_id(only_listed=True).id
    #     if not last_error and not last_updated:
    #         start = last_item - 100
    #     else:
    #         last_item = start
    #
    # start = max(0, min(start, steam_total_count - 100))

    # simple version for updating items
    start = last_item
    if start >= steam_total_count - 100 and not last_error:
        start = max(0, steam_total_count - 100)
        last_item = 0
    elif not last_error:
        last_item += 100
    print("Updating items from: " + str(start) + " to: " + str(start + 100))

    data = await get_data_json(appid, start=start, sort_column="name", sort_dir="asc")

    if not data:
        print("Error: request failed")
        last_error = True
        last_updated = False
        return data
    if not data["results"]:
        print("Error: no data")
        last_error = True
        last_updated = False
        if data["total_count"] < start:
            building = False
        return data

    last_error = False
    steam_total_count = data["total_count"]

    if len(data["results"]) < 100:
        print("less than 100")
        building = False
        last_updated = False
        return data

    filter_keys = ["name", "sell_listings", "sell_price", "icon_url", "appid"]
    data_filtered = await filter_data(data, filter_keys)

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
    if len(request_full_names) != len(database_full_names):
        print("updated some items")
    for item in database_full_names:
        if item.full_name not in request_full_names:
            set_item_listing(item.full_name, False)

    return data


def set_item_alphabetical_order(only_listed: bool = False):
    with Session(engine) as session:
        update = text(
            f"""
            UPDATE items
            SET alphabetical_order = t.rn
            FROM (
                SELECT id, ROW_NUMBER() OVER (ORDER BY lower(full_name) collate "C") AS rn
                FROM items
                WHERE is_listed = {only_listed}
            ) t WHERE t.id = items.id
            """
        )
        # update_stmt = (
        #     update(Item)
        #     .values(alphabetical_order=(
        #         select([
        #             func.row_number().over(
        #                 order_by=func.lower(Item.full_name).collate("C")
        #             )
        #         ])
        #         .where(Item.is_listed == only_listed)
        #         .label()
        #     ))
        #     .where

        session.execute(update)
        session.commit()
    return "done"


# print(set_item_alphabetical_order())


def get_items(db: Session, limit: int = 100):
    items = db.query(Item).limit(limit).all()
    return items
