from typing import List

import crud.user
import models
import schemas
from database import get_db
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/user/{username}", response_model=schemas.User, tags=["users"])
def read_user(username: str, db: Session = Depends(get_db)):
    user = crud.user.get_user_by_username(db, username)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.get("/users", response_model=List[schemas.User], tags=["users"])
def read_all_users(db: Session = Depends(get_db)):
    users = crud.user.get_all_users(db)
    print(users)
    if not users:
        raise HTTPException(status_code=404, detail="Users not found")
    return users


@router.post("/user", tags=["users"])
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.user.create_user(db=db, user=user)


@router.post("/users/{user_id}/role", tags=["users"])
def create_role_user(role: schemas.RoleCreate, user_id: int, db: Session = Depends(get_db)):
    role.user_id = user_id
    return crud.user.create_role(db=db, role=role)


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
