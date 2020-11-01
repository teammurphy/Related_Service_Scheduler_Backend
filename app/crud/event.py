import logging

import models
from custom_exceptions import InvaldEntryException
from schemas import event_schema
from sqlalchemy.orm import Session

from . import crud_base


def get_event(db: Session, event_id: int):
    return db.query(models.Event).filter(models.Event.id == event_id).first()


def get_all_events(db: Session):
    return db.query(models.Event).all()


def create_event(db: Session, event: event_schema.EventCreate):
    db_event = models.Event()
    [setattr(db_event, i[0], i[1]) for i in event]
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event


def update_event(db: Session, event_id: int, updated_event: event_schema.EventCreate):
    db_event = get_event(db, event_id)
    if db_event is None:
        return False

    logging.info(updated_event)

    [setattr(db_event, i[0], i[1]) for i in updated_event]
    db.commit()
    db.refresh(db_event)
    return True
