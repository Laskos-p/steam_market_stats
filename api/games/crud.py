from sqlalchemy import func, update
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.orm import Session

from ..database import engine
from ..models import Item
from ..utils import get_data_json
from .models import Game
from .utils import filter_data, get_game_json


def get_games(db: Session):
    games = db.query(Game).all()
    return games


def get_game_by_appid(appid: int, db: Session):
    game = db.query(Game).filter(Game.appid == appid).first()
    return game


def get_game_info(appid: int):
    # fileter keys order should match Game model order
    filter_keys = ["steam_appid", "name", "header_image"]
    game_info = get_game_json(appid)
    game_info_filtered = filter_data(game_info, filter_keys)
    return game_info_filtered


async def add_game_data(appid: int):
    game_info = get_game_info(appid)
    with Session(engine) as session:
        stmt = (
            insert(Game)
            .values(game_info)
            .on_conflict_do_update(
                index_elements=["appid"],
                set_=dict(
                    name=insert(Game).values(game_info).excluded.name,
                    header_image=insert(Game).values(game_info).excluded.header_image,
                ),
            )
        )
        session.execute(stmt)
        session.commit()

    await update_game_listed_unique_items(appid)
    try:
        await update_all_unique_items(appid)
    except Exception as e:
        print("No item data in database")
        print(e)

    return game_info


async def update_game_listed_unique_items(appid: int):
    data_json = await get_data_json(appid, count=1)
    listed_unique_items = data_json["total_count"]
    with Session(engine) as session:
        stmt = (
            update(Game)
            .where(Game.appid == appid)
            .values(listed_unique_items=listed_unique_items)
        )
        session.execute(stmt)
        session.commit()
    return


async def update_all_unique_items(appid: int):
    with Session(engine) as session:
        all_unique_items = session.query(Item).filter(Item.appid == appid).count()
        number_of_listings = (
            session.query(func.sum(Item.sell_listings))
            .filter(Item.appid == appid)
            .filter(Item.is_listed == True)
            .scalar()
        )
        value_of_listings = (
            session.query(func.sum(Item.sell_listings * Item.sell_price))
            .filter(Item.appid == appid)
            .filter(Item.is_listed == True)
            .scalar()
        )
        stmt = (
            update(Game)
            .where(Game.appid == appid)
            .values(
                all_unique_items=all_unique_items,
                number_of_listings=number_of_listings,
                value_of_listings=value_of_listings,
            )
        )
        session.execute(stmt)
        session.commit()


# print(update_all_unique_items(730))
