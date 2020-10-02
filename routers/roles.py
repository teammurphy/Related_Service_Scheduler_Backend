
from typing import List

import crud.role
import models
import schemas
from database import get_db
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/role/{role_id}", response_model=schemas.Role, tags=["role"])
def read_role(role_id: int, db: Session = Depends(get_db)):
    role = crud.role.get_role(db, role_id=role_id)
    if role is None:
        raise HTTPException(status_code=404, detail="Role not found")
    return role


@router.post("/role", tags=["role"])
def create_role(role: schemas.RoleCreate, db: Session = Depends(get_db)):
    return crud.role.create_role(db=db, role=role)


@router.delete("/role/{role_id}",  tags=["role"])
def delete_role(role_id: int, db: Session = Depends(get_db)):
    deleted = crud.role.delete_role(db=db, role_id=role_id)
    if deleted is False:
        raise HTTPException(status_code=404, detail="Role not found")
    return role_id


@router.put("/role/{role_id}", tags=["role"])
def update_role(updated_role: schemas.RoleCreate, role_id: int, db: Session = Depends(get_db)):
    updated = crud.role.update_role(
        db=db, role_id=role_id, updated_role=updated_role)
    if updated is False:
        raise HTTPException(status_code=404, detail="Role not found")
    return role_id
