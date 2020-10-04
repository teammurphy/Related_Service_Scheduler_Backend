from pydantic import BaseModel


class CaseBase(BaseModel):
    caseload_id: int
    student_id: int


class CaseCreate(CaseBase):
    pass


class Case(CaseBase):
    id: int

    class Config:
        orm_mode = True
