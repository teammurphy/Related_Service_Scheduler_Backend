import logging

import models
import schemas
from custom_exceptions import InvaldEntryException
from sqlalchemy.orm import Session

from . import crud_base


def check_mandate_inputs(mandate: schemas.MandateCreate):
    if mandate.service not in crud_base.services:
        raise InvaldEntryException(
            entered=mandate.service, allowed=crud_base.services)
    if mandate.periodicity not in crud_base.periodicitys:
        raise InvaldEntryException(
            entered=mandate.periodicity, allowed=crud_base.periodicitys)


def get_mandate(db: Session, mandate_id: int):
    return db.query(models.Mandate).filter(models.Mandate.id == mandate_id).first()


def create_mandate(db: Session, mandate: schemas.MandateCreate):
    check_mandate_inputs(mandate)

    db_mandate = models.Mandate()
    [setattr(db_mandate, i[0], i[1]) for i in mandate]
    db.add(db_mandate)
    db.commit()
    db.refresh(db_mandate)
    return db_mandate


def delete_mandate(db: Session, mandate_id: int):
    db_mandate = get_mandate(db, mandate_id)
    if db_mandate:
        db.delete(db_mandate)
        db.commit()
        return True
    else:
        return False


def update_mandate(db: Session, mandate_id: int, updated_mandate: schemas.MandateCreate):
    check_mandate_inputs(update_mandate)
    db_mandate = get_mandate(db, mandate_id)
    if db_mandate is None:
        return False
    [setattr(db_mandate, i[0], i[1]) for i in updated_mandate]
    db.commit()
    db.refresh(db_mandate)
    return True
