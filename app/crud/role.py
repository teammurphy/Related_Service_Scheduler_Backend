import logging

import models
from custom_exceptions import InvaldEntryException
from schemas import role_schema
from sqlalchemy.orm import Session

from . import crud_base


def check_role_inputs(role: role_schema.RoleCreate):
    if role.name not in crud_base.names:
        raise InvaldEntryException(
            entered=role.name, allowed=crud_base.names)
    if role.county not in crud_base.counties:
        raise InvaldEntryException(
            entered=role.county, allowed=crud_base.counties)
    if role.service not in crud_base.services:
        raise InvaldEntryException(
            entered=role.service, allowed=crud_base.services)


def get_role(db: Session, role_id: int):
    return db.query(models.Role).filter(models.Role.id == role_id).first()


def create_role(db: Session, role: role_schema.RoleCreate):
    check_role_inputs(role)
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


def update_role(db: Session, role_id: int, updated_role: role_schema.RoleCreate):
    check_role_inputs(updated_role)
    db_role = get_role(db, role_id)
    if db_role is None:
        return False

    [setattr(db_role, i[0], i[1]) for i in updated_role]
    db.commit()
    db.refresh(db_role)
    return True
