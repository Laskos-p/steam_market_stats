from pydantic import BaseModel


class ItemDB(BaseModel):
    id: int
    name: str
    weapon: str
    stattrak: bool
    quality: str
    sell_listings: int
    sell_price: int
    icon_url: str
    appid: int
