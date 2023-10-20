from pydantic import BaseModel


class Game(BaseModel):
    appid: int
    name: str
    header_image: str
    listed_unique_items: int
    all_unique_items: int
    number_of_listings: int
    value_of_listings: int
