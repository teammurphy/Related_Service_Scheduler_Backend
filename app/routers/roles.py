
from typing import List

import crud.role
import models
from database import get_db
from fastapi import APIRouter, Depends, HTTPException
from schemas import role_schema
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/role/{role_id}", response_model=role_schema.Role, tags=["role"])
def read_role(role_id: int, db: Session = Depends(get_db)):
    role = crud.role.get_role(db, role_id=role_id)
    if role is None:
        raise HTTPException(status_code=404, detail="Role not found")
    return role


@router.post("/role", tags=["role"])
def create_role(role: role_schema.RoleCreate, db: Session = Depends(get_db)):
    return crud.role.create_role(db=db, role=role)


@router.put("/role/{role_id}", tags=["role"])
def update_role(updated_role: role_schema.RoleCreate, role_id: int, db: Session = Depends(get_db)):
    updated = crud.role.update_role(
        db=db, role_id=role_id, updated_role=updated_role)
    if updated is False:
        raise HTTPException(status_code=404, detail="Role not found")
    return role_id
