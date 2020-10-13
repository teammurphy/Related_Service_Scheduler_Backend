from datetime import date, datetime
from typing import List, Optional

from pydantic import BaseModel

from .student_schema import Student


class SchoolBase(BaseModel):
    dbn: str
    district: str
    county: str
    name: str

    class Config:
        orm_mode = True


class SchoolCreate(SchoolBase):
    pass


class School(SchoolBase):
    id: int
    students: List[Student] = []


class SchoolThin(SchoolBase):
    id: int
