from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from . import models, schemas
from .crud import add_item_data
from .database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

add_item_data(730)


@app.get("/")
async def read_root():
    return {"message": "Hello World"}


@app.get("/items/{item_id}", response_model=schemas.ItemDB)
def get_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(models.Item).filter(models.Item.id == item_id).first()
    return item
