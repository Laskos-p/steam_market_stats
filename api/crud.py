from sqlalchemy import insert
from sqlalchemy.orm import Session

from .database import engine
from .models import Game, Item
from .utils import filter_data, get_data_json


async def add_item_data(appid):
    data = await get_data_json(appid)
    filter_keys = ["name", "sell_listings", "sell_price", "icon_url", "appid"]
    data_filtered = await filter_data(data, filter_keys)
    with Session(engine) as session:
        session.execute(insert(Item), data_filtered)
        session.commit()
    return data


def get_items(db: Session, limit: int = 100):
    items = db.query(Item).limit(limit).all()
    return items
