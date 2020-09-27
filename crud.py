import logging

import models
import schemas
from sqlalchemy.orm import Session


def get_user_by_username(db: Session, username: int):
    return db.query(models.User).filter(models.User.username == username).first()


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_role(db: Session, role_id: int):
    return db.query(models.Role).filter(models.Role.id == role_id).first()


def get_caseload(db: Session, caseload_id: int):
    return db.query(models.Caseload).filter(models.Caseload.id == caseload_id).first()


def get_goal(db: Session, goal_id: int):
    return db.query(models.Goal).filter(models.Goal.id == goal_id).first()


def get_mandate(db: Session, mandate_id: int):
    return db.query(models.Mandate).filter(models.Mandate.id == mandate_id).first()


def get_iep(db: Session, iep_id: int):
    return db.query(models.Iep).filter(models.Iep.id == iep_id).first()


def get_school(db: Session, school_id: str):
    return db.query(models.School).filter(models.School.id == school_id).first()


def get_student(db: Session, student_id: id):
    return db.query(models.Student).filter(models.Student.id == student_id).first()


def get_case(db: Session, case_id: id):
    return db.query(models.Case).filter(models.Case.id == case_id).first()


def get_all_students(db: Session):
    # REVIEW: look into pagenation and limit fast api docs
    logging.info(db.query(models.Student).all())
    return db.query(models.Student).all()


def get_all_users(db: Session):
    # REVIEW: see above review
    return db.query(models.User).all()


def get_all_cases(db: Session):
    return db.query(models.Case).all()


def create_user(db: Session, user: schemas.UserCreate):
    not_hasshed = user.password
    db_user = models.User(username=user.username, first_name=user.first_name,
                          last_name=user.last_name, email=user.email, hashed_password=not_hasshed)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def create_role(db: Session, role: schemas.RoleCreate, user_id: int):
    db_role = models.Role(user_role=role.user_role, user_id=user_id)
    db.add(db_role)
    db.commit()
    db.refresh(db_role)
    return db_role


def create_school(db: Session, school: schemas.SchoolCreate):
    db_school = models.School(id=school.id, district=school.district,
                              county=school.county, name=school.name)
    db.add(db_school)
    db.commit()
    db.refresh(db_school)
    return db_school


def create_student(db: Session, student: schemas.StudentCreate):
    # REVIEW: id string???

    db_student = models.Student(first_name=student.first_name, last_name=student.last_name,
                                osis=student.osis, birthdate=student.birthdate, grade=student.grade, school_id=student.school_id)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student


def create_mandate(db: Session, mandate: schemas.MandateCreate):
    db_mandate = models.Mandate(service=mandate.service, group_size=mandate.group_size, duration=mandate.duration,
                                periodicity=mandate.periodicity, frequency=mandate.frequency, interval=mandate.interval, iep_id=mandate.iep_id)
    db.add(db_mandate)
    db.commit()
    db.refresh(db_mandate)
    return db_mandate


def create_iep(db: Session, iep: schemas.IepCreate):
    db_iep = models.Iep(start_date=iep.start_date,
                        end_date=iep.end_date, student_id=iep.student_id)
    db.add(db_iep)
    db.commit()
    db.refresh(db_iep)
    return db_iep
