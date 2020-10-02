import logging

import models
import schemas
from sqlalchemy.orm import Session


def get_case(db: Session, case_id: id):
    return db.query(models.Case).filter(models.Case.id == case_id).first()


def get_all_cases(db: Session):
    return db.query(models.Case).all()


def create_case(db: Session, case: schemas.CaseCreate):
    db_case = models.Case()
    [setattr(db_case, i[0], i[1]) for i in case]
    db.add(db_case)
    db.commit()
    db.refresh(db_case)
    return db_case


def delete_case(db: Session, case_id: int):
    db_case = get_case(db, case_id)
    if db_case:
        db.delete(db_case)
        db.commit()
        return True
    else:
        return False


def update_caseload(db: Session, case_id: int, updated_case: schemas.CaseCreate):
    db_case = get_caseload(db, case_id)
    if db_case is None:
        return False

    [setattr(db_case, i[0], i[1]) for i in updated_case]
    db.commit()
    db.refresh(db_case)
    return True
