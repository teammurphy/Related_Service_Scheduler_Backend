import logging

import models
import schemas
from sqlalchemy.orm import Session


def get_mandate(db: Session, mandate_id: int):
    return db.query(models.Mandate).filter(models.Mandate.id == mandate_id).first()


def create_mandate(db: Session, mandate: schemas.MandateCreate):
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
    db_mandate = get_mandate(db, mandate_id)
    if db_mandate is None:
        return False

    [setattr(db_mandate, i[0], i[1]) for i in updated_mandate]
    db.commit()
    db.refresh(db_mandate)
    return True
