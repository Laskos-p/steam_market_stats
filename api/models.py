from sqlalchemy import Boolean, ForeignKey, Identity, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func
from sqlalchemy.sql.sqltypes import TIMESTAMP

from .database import Base


class Item(Base):
    __tablename__ = "items"

    id: Mapped[int] = mapped_column(primary_key=True)
    alphabetical_order: Mapped[int] = mapped_column(
        Integer, Identity(start=1), unique=True
    )
    full_name: Mapped[str] = mapped_column(String, unique=True)
    name: Mapped[str] = mapped_column(String)
    weapon: Mapped[str] = mapped_column(String)
    stattrak: Mapped[bool] = mapped_column(Boolean)
    quality: Mapped[str] = mapped_column(String)
    sell_listings: Mapped[int] = mapped_column(Integer)
    sell_price: Mapped[int] = mapped_column(Integer)
    icon_url: Mapped[str] = mapped_column(String)
    is_listed: Mapped[bool] = mapped_column(Boolean, default=True)

    appid: Mapped[int] = mapped_column(
        Integer, ForeignKey("games.appid", ondelete="CASCADE"), nullable=False
    )
    game: Mapped[list["Game"]] = relationship("Game")
    updated_at: Mapped[str] = mapped_column(
        TIMESTAMP, server_default=func.now(), onupdate=func.now()
    )
