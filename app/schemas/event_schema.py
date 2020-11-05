from datetime import date, datetime
from typing import Optional
from pydantic import BaseModel


class EventBase(BaseModel):
    title: Optional[str]
    dtstart: Optional[datetime]
    end_date: Optional[date]

    class Config:
        orm_mode = True


class EventCreate(EventBase):
    service: Optional[str]
    duration: Optional[int]
    periodicity: Optional[str]
    interval: Optional[int]

    mandate_id: Optional[int]
    student_id: Optional[int]
    caseload_id: Optional[int]
    school_id: Optional[int]

class Event(EventCreate):
    id: int
