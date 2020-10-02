from typing import List

import crud.mandate
import models
import schemas
from database import get_db
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/mandate", tags=["mandate"])
def create_mandate(mandate: schemas.MandateCreate, db: Session = Depends(get_db)):
    return crud.mandate.create_mandate(db=db, mandate=mandate)


@router.get("/mandate/{mandate_id}", response_model=schemas.Mandate, tags=["mandate"])
def read_mandate(mandate_id: int, db: Session = Depends(get_db)):
    mandate = crud.mandate.get_mandate(db, mandate_id=mandate_id)
    if mandate is None:
        raise HTTPException(status_code=404, detail="Mandate not found")
    return mandate


@router.put("/mandate/{mandate_id}", tags=["mandate"])
def update_mandate(updated_mandate: schemas.MandateCreate, mandate_id: int, db: Session = Depends(get_db)):
    updated = crud.mandate.update_mandate(
        db=db, mandate_id=mandate_id, updated_mandate=updated_mandate)
    if updated is False:
        raise HTTPException(status_code=404, detail="Mandate not found")
    return mandate_id


@router.delete("/mandate/{mandate_id}", tags=["mandate"])
def delete_mandate(mandate_id: int, db: Session = Depends(get_db)):
    deleted = crud.mandate.delete_mandate(db=db, mandate_id=mandate_id)
    if deleted is False:
        raise HTTPException(status_code=404, detail="Mandate not found")
    return mandate_id
