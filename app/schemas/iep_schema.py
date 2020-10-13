from datetime import date, datetime
from typing import List, Optional

from pydantic import BaseModel

from .goal_schema import Goal
from .mandate_schema import Mandate


class IepBase(BaseModel):
    start_date: datetime
    end_date: datetime

    class Config:
        orm_mode = True


class IepCreate(IepBase):
    student_id: int


class Iep(IepBase):
    id: int
    mandates: List[Mandate] = []
    goals: List[Goal] = []
