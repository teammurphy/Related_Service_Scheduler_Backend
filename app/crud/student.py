import logging
from typing import List, Optional

import models
from schemas import student_schema
from sqlalchemy.orm import Session


def get_student(db: Session, student_id: int):
    return db.query(models.Student).filter(models.Student.id == student_id).first()


def get_students_by_school_id(db: Session, school_id: int):
    return db.query(models.Student).filter(
        models.Student.school_id == school_id).all()


def get_all_students(db: Session):
    # REVIEW: look into pagenation and limit fast api docs
    logging.info(db.query(models.Student).all())
    return db.query(models.Student).all()


def get_students_id_by_caseload(db: Session, caseload_id: int):
    return db.query(models.Student).join(models.Student.cases, aliased=True).filter_by(caseload_id=caseload_id).distinct(models.Student.id).all()


def get_student_by_caseload_with_caseID(db: Session, caseload_id: int):
    return db.query(models.Student, models.Case.id).join(models.Student.cases, aliased=True).filter_by(caseload_id=caseload_id).distinct(models.Student.id).all()


def get_students_by_caseload_with_mandates(db: Session, caseload_id: int):
    result = []
    students = get_students_id_by_caseload(db, caseload_id)
    for student in students:
        if student.ieps:
            mandates = db.query(models.Mandate).filter_by(
                iep_id=student.ieps.id).all()
            result.append((student, mandates))
        else:
            result.append((student, []))
    return result


def create_student(db: Session, student: student_schema.StudentCreate):
    db_student = models.Student()
    [setattr(db_student, i[0], i[1]) for i in student]
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student


def delete_student(db: Session, student_id: int):
    db_student = get_student(db, student_id)
    if db_student:
        db.delete(db_student)
        db.commit()
        return True
    else:
        return False


def update_student(db: Session, student_id: int, updated_student: student_schema.StudentCreate):
    db_student = get_student(db, student_id)
    if db_student is None:
        return False

    [setattr(db_student, i[0], i[1]) for i in updated_student]
    db.commit()
    db.refresh(db_student)
    return True
