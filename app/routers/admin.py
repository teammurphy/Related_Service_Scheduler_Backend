import logging
from typing import List

import crud.role
import crud.user
import models
from authentication import get_current_active_user
from database import get_db
from fastapi import APIRouter, Depends, HTTPException, Security
from schemas import role_schema, user_schema
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/admin/users", response_model=List[user_schema.UserWithRoles], tags=["admin"])
def admin_read_all_users(current_user: user_schema.User = Security(get_current_active_user, scopes=["admin"]), db: Session = Depends(get_db)):
    users = crud.user.get_all_users(db)
    print(users)
    if not users:
        raise HTTPException(status_code=404, detail="Users not found")
    return users


@router.post("/admin/{user_id}/role", tags=["admin"])
def admin_add_role_to_user(role: role_schema.RoleCreate, user_id: int, current_user: user_schema.User = Security(get_current_active_user, scopes=["admin"]), db: Session = Depends(get_db)):

    if not crud.user.check_user_exist_by_id(db, user_id):
        raise HTTPException(status_code=404, detail="Users not found")

    role.user_id = user_id
    return crud.role.create_role(db=db, role=role)


@router.delete("/admin/role/{role_id}", tags=["admin"])
def delete_role(role_id: int, current_user: user_schema.User = Security(get_current_active_user, scopes=["admin"]), db: Session = Depends(get_db)):
    deleted = crud.role.delete_role(db=db, role_id=role_id)
    if deleted is False:
        raise HTTPException(status_code=404, detail="Role not found")
    return role_id
