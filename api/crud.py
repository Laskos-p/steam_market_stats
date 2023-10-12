import datetime
import random

from sqlalchemy import select
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.orm import Session

from .database import engine
from .models import Game, Item
from .utils import filter_data, get_data_json

# FIXME: On app startup, check how many items are in the database and start from there
# start = 0


async def add_item_data(appid):
    # global start
    with Session(engine) as session:
        start = session.query(Item).count()
    data = await get_data_json(appid, start=start, sort_column="name", sort_dir="asc")
    # FIXME: Get better way to check if data is empty
    if not data:
        print("request failed")
        return data
    if not data["results"]:
        print("no data")
        return data
    filter_keys = ["name", "sell_listings", "sell_price", "icon_url", "appid"]
    data_filtered = await filter_data(data, filter_keys)
    # FIXME: Move this to filter_data
    for item in data_filtered:
        item["updated_at"] = datetime.datetime.now()

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
                ),
            )
        )
        session.execute(stmt)
        print("execution complete")
        session.commit()
    # start += 1
    return data


def get_items(db: Session, limit: int = 100):
    items = db.query(Item).limit(limit).all()
    return items
