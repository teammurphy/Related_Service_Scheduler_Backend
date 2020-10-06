from typing import List

import crud.caseload
import models
from database import get_db
from fastapi import APIRouter, Depends, HTTPException
from schemas import caseload_schema
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/caseload", tags=["caseload"])
def create_caseload(caseload: caseload_schema.CaseloadCreate, db: Session = Depends(get_db)):
    return crud.caseload.create_caseload(db=db, caseload=caseload)


@router.get("/caseload/{caseload_id}", response_model=caseload_schema.Caseload, tags=["caseload"])
def read_caseload(caseload_id: int, db: Session = Depends(get_db)):
    caseload = crud.caseload.get_caseload(db, caseload_id=caseload_id)
    if caseload is None:
        raise HTTPException(status_code=404, detail="Caseload not found")
    return caseload


@router.put("/caseload/{caseload_id}", tags=["caseload"])
def update_caseload(updated_caseload: caseload_schema.CaseloadCreate, caseload_id: int, db: Session = Depends(get_db)):
    updated = crud.caseload.update_caseload(
        db=db, caseload_id=caseload_id, updated_caseload=updated_caseload)
    if update is False:
        raise HTTPException(status_code=404, detail="caseload not found")
    return caseload_id


@router.delete("/caseload/{caseload_id}", tags=["caseload"])
def delete_caseload(caseload_id: int, db: Session = Depends(get_db)):
    deleted = crud.caseload.delete_caseload(db=db, caseload_id=caseload_id)
    if deleted is False:
        raise HTTPException(status_code=404, detail="Caseload not found")
    return caseload_id
