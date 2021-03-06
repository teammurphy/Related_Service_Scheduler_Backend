import logging

import models
from custom_exceptions import InvaldEntryException
from schemas import caseload_schema
from sqlalchemy.orm import Session

from . import crud_base


def check_caseload_inputs(caseload: caseload_schema.CaseloadCreate):
    if caseload.service not in crud_base.services:
        raise InvaldEntryException(
            entered=caseload.service, allowed=crud_base.services)


def get_caseload(db: Session, caseload_id: int):
    return db.query(models.Caseload).filter(models.Caseload.id == caseload_id).first()


def get_caseloads_by_user_id(db: Session, user_id: int):
    return db.query(models.Caseload).filter(models.Caseload.user_id == user_id).all()


def create_caseload(db: Session, caseload: caseload_schema.CaseloadCreate):
    check_caseload_inputs(caseload)
    db_caseload = models.Caseload()
    [setattr(db_caseload, i[0], i[1]) for i in caseload]
    db.add(db_caseload)
    db.commit()
    db.refresh(db_caseload)
    return db_caseload


def delete_caseload(db: Session, caseload_id: int):
    db_caseload = get_caseload(db, caseload_id)
    if db_caseload:
        db.delete(db_caseload)
        db.commit()
        return True
    else:
        return False


def update_caseload(db: Session, caseload_id: int, updated_caseload: caseload_schema.CaseloadCreate):
    check_caseload_inputs(updated_caseload)
    db_caseload = get_caseload(db, caseload_id)
    if db_caseload is None:
        return False

    [setattr(db_caseload, i[0], i[1]) for i in updated_caseload]
    db.commit()
    db.refresh(db_caseload)
    return True
