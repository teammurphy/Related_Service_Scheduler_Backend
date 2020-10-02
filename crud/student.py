import logging

import models
import schemas
from sqlalchemy.orm import Session


def get_student(db: Session, student_id: id):
    return db.query(models.Student).filter(models.Student.id == student_id).first()


def get_all_students(db: Session):
    # REVIEW: look into pagenation and limit fast api docs
    logging.info(db.query(models.Student).all())
    return db.query(models.Student).all()


def create_student(db: Session, student: schemas.StudentCreate):
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


def update_student(db: Session, student_id: int, updated_student: schemas.StudentCreate):
    db_student = get_student(db, student_id)
    if db_student is None:
        return False

    [setattr(db_student, i[0], i[1]) for i in updated_student]
    db.commit()
    db.refresh(db_student)
    return True
