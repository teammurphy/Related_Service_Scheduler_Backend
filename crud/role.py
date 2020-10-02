import logging

import models
import schemas
from sqlalchemy.orm import Session


def get_role(db: Session, role_id: int):
    return db.query(models.Role).filter(models.Role.id == role_id).first()


def create_role(db: Session, role: schemas.RoleCreate):
    db_role = models.Role()
    [setattr(db_role, i[0], i[1]) for i in role]
    db.add(db_role)
    db.commit()
    db.refresh(db_role)
    return db_role


def delete_role(db: Session, role_id: int):
    db_role = get_role(db, role_id)
    if db_role:
        db.delete(db_role)
        db.commit()
        return True
    else:
        return False


def update_role(db: Session, role_id: int, updated_role: schemas.RoleCreate):
    db_role = get_role(db, role_id)
    if db_role is None:
        return False

    [setattr(db_role, i[0], i[1]) for i in updated_role]
    db.commit()
    db.refresh(db_role)
    return True
