from datetime import date, datetime

from pydantic import BaseModel


class EventBase(BaseModel):
    title: str
    dtstart: datetime
    end_date: date

    class Config:
        orm_mode = True


class EventCreate(EventBase):
    service: str
    duration: int
    periodicity: str
    interval: int

    mandate_id: int
    student_id: int
    caseload_id: int
    school_id: int


class Event(EventCreate):
    id: int
