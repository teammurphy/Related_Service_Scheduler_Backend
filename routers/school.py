from typing import List

import crud.school
import models
import schemas
from database import get_db
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/school", tags=["school"])
def create_school(school: schemas.SchoolCreate, db: Session = Depends(get_db)):
    return crud.school.create_school(db=db, school=school)


@router.get("/school/{school_id}", response_model=schemas.School, tags=["school"])
def read_school(school_id: str, db: Session = Depends(get_db)):
    school = crud.school.get_school(db, school_id=school_id)
    if school is None:
        raise HTTPException(status_code=404, detail="School not found")
    return school


@router.put("/school/{school_id}", tags=["school"])
def update_school(school: schemas.SchoolCreate, school_id: str, db: Session = Depends(get_db)):
    updated = crud.school.update_school(
        db=db, school_id=school_id, school=school)
    if updated is False:
        raise HTTPException(status_code=404, detail="School not found")
    return school.id


@router.delete("/school/{school_id}", tags=["school"])
def delete_school(school_id: str, db: Session = Depends(get_db)):
    deleted = crud.school.delete_school(db=db, school_id=school_id)
    if deleted is False:
        raise HTTPException(status_code=404, detail="School not found")
    return school_id
