from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from ..database import Base


class Game(Base):
    __tablename__ = "games"

    appid: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String)
    header_image: Mapped[str] = mapped_column(String)
    listed_unique_items: Mapped[int] = mapped_column(Integer, default=0)
    all_unique_items: Mapped[int] = mapped_column(Integer, default=0)
    number_of_listings: Mapped[int] = mapped_column(Integer, default=0)
    value_of_listings: Mapped[int] = mapped_column(Integer, default=0)
