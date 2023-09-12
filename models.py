from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Game(DeclarativeBase):
    __tablename__ = "games"

    appid: Mapped[int] = mapped_column(primary_key=True)
    game_name: Mapped[str] = mapped_column(String)


class Item(DeclarativeBase):
    __tablename__ = "items"

    id: Mapped[int] = mapped_column(primary_key=True)
    item_name: Mapped[str] = mapped_column(String)
    sell_listings = Mapped[int] = mapped_column()

    appid: Mapped[int] = mapped_column(ForeignKey("games.appid"))