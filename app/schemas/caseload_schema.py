from typing import List, Optional

from pydantic import BaseModel

from .case_schema import Case


class CaseloadBase(BaseModel):
    title: str
    service: str

    class Config:
        orm_mode = True


class CaseloadCreate(CaseloadBase):
    user_id: int


class Caseload(CaseloadBase):
    id: int
    cases: List[Case] = []


class CaseloadThin(CaseloadBase):
    id: int
