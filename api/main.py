import asyncio
from contextlib import asynccontextmanager
from time import time_ns
from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import engine, get_db

models.Base.metadata.create_all(bind=engine)


@asynccontextmanager
async def lifespan(app: FastAPI):
    # run task before app startup
    task = asyncio.create_task(fetch_data())
    # run app
    yield
    # on shutdown close task
    task.cancel()


app = FastAPI(lifespan=lifespan)

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
    while True:
        print("Fetching data...")
        time = time_ns()
        await crud.add_item_data(730)
        print(f"Data fetched {time_ns() - time/10**9} s")
        await asyncio.sleep(30)


# deprecated
# global task
# @app.on_event("startup")
# async def startup():
#     global task
#     task = asyncio.create_task(fetch_data())
#
#
# @app.on_event("shutdown")
# def shutdown():
#     global task
#     task.cancel()


@app.get("/")
async def read_root():
    return {"message": "Hello World"}


@app.get("/items", response_model=list[schemas.ItemDB])
def get_items(limit: Annotated[int, Query()] = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, limit)
    print("co jest")
    if not items:
        raise HTTPException(status_code=400, detail="There are no items")
    return items


@app.get("/items/{item_id}", response_model=schemas.ItemDB)
def get_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if not item:
        raise HTTPException(status_code=400, detail="Item doesnt exist")
    return item
