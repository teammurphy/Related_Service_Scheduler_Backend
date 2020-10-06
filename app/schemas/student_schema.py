from datetime import date, datetime
from typing import List, Optional

from pydantic import BaseModel

from .iep_schema import Iep


class StudentBase(BaseModel):
    first_name: str
    last_name: str
    osis: str
    birthdate: date
    grade: str

    class Config:
        orm_mode = True


class StudentCreate(StudentBase):
    school_id: str


class Student(StudentBase):
    id: int
    ieps: List[Iep] = []


class StudentCase(StudentBase):
    id: int
    school_id: str
    case_id: int
