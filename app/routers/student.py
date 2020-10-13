import logging
from typing import List, Optional

import crud.student
import models
from database import get_db
from fastapi import APIRouter, Depends, HTTPException, Query
from schemas import student_schema
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/student/{student_id}", response_model=student_schema.Student, tags=["student"])
def read_student(student_id: int,  db: Session = Depends(get_db)):
    student = crud.student.get_student(db, student_id=student_id)
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return student


@router.get("/students", response_model=List[student_schema.Student], tags=["student"])
def read_all_students(db: Session = Depends(get_db)):
    students = crud.student.get_all_students(db)
    if not students:
        raise HTTPException(status_code=404, detail="Students not found")
    return students


@router.get("/students/caseload/{caseload_id}", response_model=List[student_schema.StudentThin], tags=["student"])
def read_students_by_caseload(caseload_id: int, db: Session = Depends(get_db)):
    result = []
    li_tup_students_caseid = crud.student.get_student_by_caseload(
        db, caseload_id)

    if not li_tup_students_caseid:
        raise HTTPException(status_code=404, detail="Students not found")

    def add_case_id_to_student(tup):
        setattr(tup[0], 'case_id', tup[1])
        return tup[0]

    result = list(map(add_case_id_to_student, li_tup_students_caseid))

    return result


@router.get("/students/schools/{school_id}", response_model=List[student_schema.StudentWithFullName], tags=["student"])
def read_students_by_school(school_id: int, db: Session = Depends(get_db)):

    students = crud.student.get_students_by_school_id(db, school_id)
    if not students:
        raise HTTPException(status_code=404, detail="Students not found")

    def add_fullname(student_obj):
        student_obj.full_name = f'{student_obj.first_name} {student_obj.last_name}'
        return student_obj

    students = list(map(add_fullname, students))

    return students


@router.post("/student", tags=["student"])
def create_student(student: student_schema.StudentCreate, db: Session = Depends(get_db)):
    return crud.student.create_student(db=db, student=student)


@router.delete("/student/{student_id}", tags=["student"])
def delete_student(student_id: int, db: Session = Depends(get_db)):
    deleted = crud.student.delete_student(db=db, student_id=student_id)
    if deleted is False:
        raise HTTPException(status_code=404, detail="Student not found")
    return student_id


@router.put("/student/{student_id}", tags=["student"])
def update_student(updated_student: student_schema.StudentCreate, student_id: int, db: Session = Depends(get_db)):
    updated = crud.student.update_student(
        db=db, student_id=student_id, updated_student=updated_student)
    if updated is False:
        raise HTTPException(status_code=404, detail="Student not found")
    return student_id
