from typing import List

import crud.student
import models
import schemas
from database import get_db
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/student/{student_id}", response_model=schemas.Student, tags=["student"])
def read_student(student_id: int,  db: Session = Depends(get_db)):
    student = crud.student.get_student(db, student_id=student_id)
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return student


@router.get("/students", response_model=List[schemas.Student], tags=["student"])
def read_all_students(db: Session = Depends(get_db)):
    students = crud.student.get_all_students(db)
    if not students:
        raise HTTPException(status_code=404, detail="Students not found")
    return students


@router.post("/student", tags=["student"])
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    return crud.student.create_student(db=db, student=student)


@router.delete("/student/{student_id}", tags=["student"])
def delete_student(student_id: int, db: Session = Depends(get_db)):
    deleted = crud.student.delete_student(db=db, student_id=student_id)
    if deleted is False:
        raise HTTPException(status_code=404, detail="Student not found")
    return student_id


@router.put("/student/{student_id}", tags=["student"])
def update_student(updated_student: schemas.StudentCreate, student_id: int, db: Session = Depends(get_db)):
    updated = crud.student.update_student(
        db=db, student_id=student_id, updated_student=updated_student)
    if updated is False:
        raise HTTPException(status_code=404, detail="Student not found")
    return student_id
