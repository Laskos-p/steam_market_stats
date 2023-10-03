from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, Query
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# crud.add_item_data(730)


@app.get("/")
async def read_root():
    return {"message": "Hello World"}


@app.get("/items", response_model=list[schemas.ItemDB])
def get_items(limit: Annotated[int, Query()] = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, limit)
    if not items:
        raise HTTPException(status_code=400, detail="There are no items")
    return items


@app.get("/items/{item_id}", response_model=schemas.ItemDB)
def get_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if not item:
        raise HTTPException(status_code=400, detail="Item doesnt exist")
    return item
