from typing import List

import crud
import models
import schemas
from database import get_db
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/iep", tags=["iep"])
def create_iep(iep: schemas.IepCreate, db: Session = Depends(get_db)):
    return crud.create_iep(db=db, iep=iep)


@router.get("/iep/{iep_id}", response_model=schemas.Iep, tags=["iep"])
def read_iep(iep_id: int, db: Session = Depends(get_db)):
    iep = crud.get_iep(db, iep_id=iep_id)
    if iep is None:
        raise HTTPException(status_code=404, detail="Iep not found")
    return iep


@router.put("/iep/{iep_id}", tags=["iep"])
def update_iep(updated_iep: schemas.IepCreate, iep_id: int, db: Session = Depends(get_db)):
    updated = crud.update_iep(db=db, iep_id=iep_id, updated_iep=updated_iep)
    if update is False:
        raise HTTPException(status_code=404, detail="Iep not found")
    return iep_id


@router.delete("/iep/{iep_id}", tags=["iep"])
def delete_iep(iep_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_iep(db=db, iep_id=iep_id)
    if deleted is False:
        raise HTTPException(status_code=404, detail="Iep not found")
    return iep_id
