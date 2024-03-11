from sqlalchemy import Boolean, ForeignKey, Identity, Integer, String, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func
from sqlalchemy.sql.sqltypes import TIMESTAMP

from .database import Base
# from .games.models import Game

import enum


class ItemType(enum.Enum):
    weapon = "weapon"
    case = "case"
    key = "key"
    sticker = "sticker"
    graffiti = "graffiti"
    music_kit = "music"
    agent = "agent"
    capsule = "capsule"
    other = "other"


class Item(Base):
    __tablename__ = "items"

    item_id: Mapped[int] = mapped_column(primary_key=True)
    alphabetical_order: Mapped[int] = mapped_column(Integer, Identity(start=1))
    full_name: Mapped[str] = mapped_column(String, unique=True)
    type: Mapped[enum] = mapped_column(Enum(ItemType))
    updated_at: Mapped[str] = mapped_column(TIMESTAMP, server_default=func.now())


class Weapon(Base):
    __tablename__ = "weapons"

    weapon_id: Mapped[int] = mapped_column(primary_key=True)
    item_id: Mapped[int] = mapped_column(Integer, ForeignKey("items.item_id", ondelete="CASCADE"), nullable=False)
    name: Mapped[str] = mapped_column(String, unique=True)
    weapon_type: Mapped[str] = mapped_column(String)
    weapon_name: Mapped[str] = mapped_column(String)
    stattrak: Mapped[bool] = mapped_column(Boolean)
    quality: Mapped[str] = mapped_column(String)
    photo_url: Mapped[str] = mapped_column(String)


class PriceHistory(Base):
    __tablename__ = "price_history"

    price_id: Mapped[int] = mapped_column(primary_key=True)
    item_id: Mapped[int] = mapped_column(Integer, ForeignKey("items.item_id", ondelete="CASCADE"), nullable=False)
    price: Mapped[int] = mapped_column(Integer)
    date: Mapped[str] = mapped_column(TIMESTAMP, server_default=func.now())


# class Item(Base):
#     __tablename__ = "items"
#
#     id: Mapped[int] = mapped_column(primary_key=True)
#     alphabetical_order: Mapped[int] = mapped_column(Integer, Identity(start=1))
#     full_name: Mapped[str] = mapped_column(String, unique=True)
#     name: Mapped[str] = mapped_column(String)
#     weapon: Mapped[str] = mapped_column(String)
#     stattrak: Mapped[bool] = mapped_column(Boolean)
#     quality: Mapped[str] = mapped_column(String)
#     sell_listings: Mapped[int] = mapped_column(Integer)
#     sell_price: Mapped[int] = mapped_column(Integer)
#     icon_url: Mapped[str] = mapped_column(String)
#     is_listed: Mapped[bool] = mapped_column(Boolean, default=True)
#
#     appid: Mapped[int] = mapped_column(
#         Integer, ForeignKey("games.appid", ondelete="CASCADE"), nullable=False
#     )
#     game: Mapped[list["Game"]] = relationship("Game")
#     updated_at: Mapped[str] = mapped_column(TIMESTAMP, server_default=func.now())
