import asyncio
from contextlib import asynccontextmanager
from time import time_ns
from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import engine, get_db
# from .games import models as game_model
# from .games.crud import add_game_data
# from .games.router import router as games_router

models.Base.metadata.create_all(bind=engine)
# game_model.Base.metadata.create_all(bind=engine)


@asynccontextmanager
async def lifespan(app: FastAPI):
    # run task before app startup
    task = asyncio.create_task(fetch_data())

    try:
        yield
    finally:
        # on shutdown close task
        task.cancel()
        try:
            await task
        except asyncio.CancelledError:
            pass


app = FastAPI(lifespan=lifespan)

# app.include_router(games_router)

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


async def fetch_data():
    args = ()
    # await add_game_data(730)
    while True:
        print("Fetching data...")
        time = time_ns()
        args = await crud.add_item_data(730, *args)
        print(f"Data fetched {(time_ns() - time)/10**9} s")
        await asyncio.sleep(10)


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
