from typing import List

import crud.role
import crud.user
import models
import schemas
from authentication import get_current_active_user
from database import get_db
from fastapi import APIRouter, Depends, HTTPException, Security
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/admin/users", response_model=List[schemas.User], tags=["admin"])
def admin_read_all_users(current_user: schemas.User = Security(get_current_active_user, scopes=["admin"]), db: Session = Depends(get_db)):
    users = crud.user.get_all_users(db)
    print(users)
    if not users:
        raise HTTPException(status_code=404, detail="Users not found")
    return users


@router.post("/admin/{user_id}/role", tags=["admin"])
def admin_add_role_to_user(role: schemas.RoleAddToUser, user_id: int, current_user: schemas.User = Security(get_current_active_user, scopes=["admin"]), db: Session = Depends(get_db)):
    # TODO: make sure user exists
    role.user_id = user_id
    return crud.role.create_role(db=db, role=role)
