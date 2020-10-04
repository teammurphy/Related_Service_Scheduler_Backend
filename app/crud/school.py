import logging

import models
import schemas
from custom_exceptions import InvaldEntryException
from sqlalchemy.orm import Session

from . import crud_base


def get_school(db: Session, school_id: str):
    return db.query(models.School).filter(models.School.id == school_id).first()


def create_school(db: Session, school: schemas.SchoolCreate):
    if school.county not in crud_base.counties:
        raise InvaldEntryException(
            entered=school.county, allowed=crud_base.counties)
    db_school = models.School()
    [setattr(db_school, i[0], i[1]) for i in school]
    db.add(db_school)
    db.commit()
    db.refresh(db_school)
    return db_school


def delete_school(db: Session, school_id: str):
    db_school = get_school(db, school_id)
    if db_school:
        db.delete(db_school)
        db.commit()
        return True
    else:
        return False


def update_school(db: Session, school_id: int, updated_school: schemas.SchoolCreate):
    db_school = get_school(db, school_id)
    if db_school is None:
        return False

    [setattr(db_school, i[0], i[1]) for i in updated_school]
    db.commit()
    db.refresh(db_school)
    return True
