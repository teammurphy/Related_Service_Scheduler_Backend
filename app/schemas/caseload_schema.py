from typing import List, Optional

from pydantic import BaseModel

from .case_schema import Case


class CaseloadBase(BaseModel):
    title: str
    service: str


class CaseloadCreate(CaseloadBase):
    user_id: int


class Caseload(CaseloadBase):
    id: int
    cases: List[Case] = []

    class Config:
        orm_mode = True