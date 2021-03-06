from typing import List

import crud.iep
import models
from database import get_db
from fastapi import APIRouter, Depends, HTTPException
from schemas import iep_schema
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/iep", tags=["iep"])
def create_iep(iep: iep_schema.IepCreate, db: Session = Depends(get_db)):
    return crud.iep.create_iep(db=db, iep=iep)


@router.get("/iep/{iep_id}", response_model=iep_schema.Iep, tags=["iep"])
def read_iep(iep_id: int, db: Session = Depends(get_db)):
    iep = crud.iep.get_iep(db, iep_id=iep_id)
    if iep is None:
        raise HTTPException(status_code=404, detail="Iep not found")
    return iep


@router.put("/iep/{iep_id}", tags=["iep"])
def update_iep(updated_iep: iep_schema.IepCreate, iep_id: int, db: Session = Depends(get_db)):
    updated = crud.iep.update_iep(
        db=db, iep_id=iep_id, updated_iep=updated_iep)
    if update is False:
        raise HTTPException(status_code=404, detail="Iep not found")
    return iep_id


@router.delete("/iep/{iep_id}", tags=["iep"])
def delete_iep(iep_id: int, db: Session = Depends(get_db)):
    deleted = crud.iep.delete_iep(db=db, iep_id=iep_id)
    if deleted is False:
        raise HTTPException(status_code=404, detail="Iep not found")
    return iep_id
