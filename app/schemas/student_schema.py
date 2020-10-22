from datetime import date, datetime
from typing import List, Optional

from pydantic import BaseModel

from .iep_schema import Iep
from .mandate_schema import Mandate


class StudentBase(BaseModel):
    first_name: Optional[str] = None
    last_name: str
    osis: str
    birthdate: date
    grade: str

    class Config:
        orm_mode = True


class StudentCreate(StudentBase):
    school_id: int


class Student(StudentBase):
    id: int
    ieps: List[Iep] = []


class StudentThin(StudentBase):
    id: int
    school_id: int
    case_id: int


class StudentWithFullName(StudentBase):
    id: int
    full_name: str


class StudentMandates(StudentBase):
    id: int
    school_id: int
    mandates: Optional[List[Mandate]] = []
