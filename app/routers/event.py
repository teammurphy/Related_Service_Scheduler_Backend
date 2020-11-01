import logging
from typing import List

import crud.event
import models
from database import get_db
from fastapi import APIRouter, Depends, HTTPException
from schemas import event_schema
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/event", tags=['event'])
def create_event(event: event_schema.EventCreate, db: Session = Depends(get_db)):
    return crud.event.create_event(db=db, event=event)


@router.put("/event/{event_id}", tags=['event'])
def update_event(updated_event: event_schema.EventCreate, event_id: int, db: Session = Depends(get_db)):
    logging.info(event_id)
    updated = crud.event.update_event(
        db=db, event_id=event_id, updated_event=updated_event)
    if updated is False:
        raise HTTPException(status_code=404, detail="event not found")
    return event_id


@router.get("/events", response_model=List[event_schema.Event], tags=['event'])
def read_events(db: Session = Depends(get_db)):
    events = crud.event.get_all_events(db)
    if events is None:
        raise HTTPException(status_code=404, detail='No events')
    return events


@router.get("/events/caseload/{caseload_id}", response_model=List[event_schema.Event], tags=['event'])
def read_events_by_caseload_id(caseload_id: int, db: Session = Depends(get_db)):
    events = crud.event.get_events_by_caseload_id(
        db=db, caseload_id=caseload_id)
    if not events:
        raise HTTPException(status_code=404, detail='No events')
    return events


@router.get("/events/student/{student_id}", response_model=List[event_schema.Event], tags=['event'])
def read_events_by_student_id(student_id: int, db: Session = Depends(get_db)):
    events = crud.event.get_events_by_student_id(db=db, student_id=student_id)
    if not events:
        raise HTTPException(status_code=404, detail='No events')
    return events


@router.get("/events/school/{school_id}", response_model=List[event_schema.Event], tags=['event'])
def read_events_by_school_id(school_id: int, db: Session = Depends(get_db)):
    events = crud.event.get_events_by_school_id(db=db, school_id=school_id)
    if not events:
        raise HTTPException(status_code=404, detail='No events')
    return events
