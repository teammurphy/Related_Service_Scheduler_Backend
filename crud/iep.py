import logging

import models
import schemas
from sqlalchemy.orm import Session


def get_iep(db: Session, iep_id: int):
    return db.query(models.Iep).filter(models.Iep.id == iep_id).first()


def create_iep(db: Session, iep: schemas.IepCreate):
    db_iep = models.Iep()
    [setattr(db_iep, i[0], i[1]) for i in iep]
    db.add(db_iep)
    db.commit()
    db.refresh(db_iep)
    return db_iep


def delete_iep(db: Session, iep_id: int):
    db_iep = get_iep(db, iep_id)
    if db_iep:
        db.delete(db_iep)
        db.commit()
        return True
    else:
        return False


def update_iep(db: Session, iep_id: int, updated_iep: schemas.IepCreate):
    db_iep = get_iep(db, iep_id)
    if db_iep is None:
        return False

    [setattr(db_iep, i[0], i[1]) for i in updated_iep]
    db.commit()
    db.refresh(db_iep)
    return True
