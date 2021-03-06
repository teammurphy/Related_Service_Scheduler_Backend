from datetime import date, datetime
from typing import List, Optional

from pydantic import BaseModel

from .goal_schema import Goal
from .mandate_schema import Mandate


class IepBase(BaseModel):
    start_date: date
    end_date: date

    class Config:
        orm_mode = True


class IepCreate(IepBase):
    student_id: int


class Iep(IepBase):
    id: int
    mandates: List[Mandate] = []
    goals: List[Goal] = []


class IepThin(IepBase):
    student_id: int
    id: int
