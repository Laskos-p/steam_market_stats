from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

Base = declarative_base()


class Game(Base):
    __tablename__ = "games"

    appid: Mapped[int] = mapped_column(primary_key=True)
    game_name: Mapped[str] = mapped_column(String)
    total_item_count: Mapped[int] = mapped_column(Integer)


class Item(Base):
    __tablename__ = "items"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String)
    sell_listings: Mapped[int] = mapped_column(Integer)
    sell_price: Mapped[int] = mapped_column(Integer)
    icon_url: Mapped[str] = mapped_column(String)

    appid: Mapped[int] = mapped_column(
        Integer, ForeignKey("games.appid", ondelete="CASCADE"), nullable=False
    )
    game: Mapped[list["Game"]] = relationship("Game")
