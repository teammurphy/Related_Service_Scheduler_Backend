from typing import List

import crud.user
import models
from database import get_db
from fastapi import APIRouter, Depends, HTTPException
from schemas import role_schema, user_schema
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/user/{username}", response_model=user_schema.User, tags=["users"])
def read_user(username: str, db: Session = Depends(get_db)):
    user = crud.user.get_user_by_username(db, username)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.get("/users", response_model=List[user_schema.UserThin], tags=["users"])
def read_all_users(db: Session = Depends(get_db)):
    users = crud.user.get_all_users(db)
    if not users:
        raise HTTPException(status_code=404, detail="Users not found")
    return users


@router.post("/user", tags=["users"])
def create_user(user: user_schema.UserCreate, db: Session = Depends(get_db)):
    return crud.user.create_user(db=db, user=user)


@router.delete("/user/{username}", tags=["users"])
def delete_user(username: str, db: Session = Depends(get_db)):
    deleted = crud.user.delete_user_by_username(db=db, username=username)
    if deleted is False:
        raise HTTPException(status_code=404, detail="Username not found")
    return username


@router.put("/user/{username}", tags=["users"])
def update_user(username: str, db: Session = Depends(get_db)):
    # TODO: finish this
    pass
