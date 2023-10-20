from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..database import get_db
from . import crud, schemas

router = APIRouter(
    prefix="/games",
    tags=["games"],
)


@router.get("/", response_model=list[schemas.Game])
async def read_games(db: Session = Depends(get_db)):
    games = crud.get_games(db)
    if not games:
        raise HTTPException(status_code=400, detail="There are no games")
    return games


@router.get("/{appid}")
async def read_game(appid: int, db: Session = Depends(get_db)):
    game = crud.get_game_by_appid(appid, db)
    if not game:
        raise HTTPException(status_code=400, detail="Game doesn't exist")
    return game


# temporary
@router.get("/add/{appid}")
async def add_game(appid: int):
    added_game = await crud.add_game_data(appid)
    return added_game
