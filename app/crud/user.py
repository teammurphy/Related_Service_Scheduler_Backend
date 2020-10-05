import logging

import authentication
import models
from schemas import user_schema
from sqlalchemy import exists
from sqlalchemy.orm import Session


def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()


def check_user_exist_by_id(db: Session, user_id: int):
    return db.query(exists().where(models.User.id == user_id)).scalar()


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_all_users(db: Session):
    # REVIEW: see above review
    return db.query(models.User).all()


def get_providers_by_district_and_service(db: Session, district: str, service: str):
    return db.query(models.User).join(models.User.roles, aliased=True).filter_by(district=district, service=service).all()


def create_user(db: Session, user: user_schema.UserCreate):
    hashed_password = authentication.get_password_hash(user.password)
    db_user = models.User(hashed_password=hashed_password, disabled=False)
    [setattr(db_user, i[0], i[1]) for i in user]
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user_by_username(db: Session, username: str):
    db_user = get_user_by_username(db, username)
    if db_user:
        db.delete(db_user)
        db.commit()
        return True
    else:
        return False


def update_user(db: Session, user_id: int, updated_user: user_schema.UserCreate):
    db_user = get_user(db, user_id)
    if db_user is None:
        return False

    [setattr(db_user, i[0], i[1]) for i in updated_user]
    db.commit()
    db.refresh(db_user)
    return True
