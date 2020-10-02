from datetime import date, datetime
from typing import List, Optional

from pydantic import BaseModel


class GoalBase(BaseModel):
    goal: str
    criteria: str
    method: str
    schedule: str


class GoalCreate(GoalBase):
    iep_id: int


class Goal(GoalBase):
    id: int


class MandateBase(BaseModel):
    service: str
    group_size: int
    duration: int
    periodicity: str
    frequency: int
    interval: int


class MandateCreate(MandateBase):
    iep_id: int


class Mandate(MandateBase):
    id: int


class IepBase(BaseModel):
    start_date: datetime
    end_date: datetime


class IepCreate(IepBase):
    student_id: int


class Iep(IepBase):
    id: int
    mandates: List[Mandate] = []
    goals: List[Goal] = []

    class Config:
        orm_mode = True


class StudentBase(BaseModel):
    first_name: str
    last_name: str
    osis: str
    birthdate: date
    grade: str


class StudentCreate(StudentBase):
    school_id: str


class Student(StudentBase):
    id: int
    ieps: List[Iep] = []

    class Config:
        orm_mode = True


class SchoolBase(BaseModel):
    district: str
    county: str
    name: str
    id: str


class SchoolCreate(SchoolBase):
    pass


class School(SchoolBase):
    students: List[Student] = []

    class Config:
        orm_mode = True


class RoleBase(BaseModel):
    name: str
    school: str
    district: str
    county: str


class RoleCreate(RoleBase):
    user_id: int


class Role(RoleBase):
    id: int

    class Config:
        orm_mode = True


class CaseBase(BaseModel):
    caseload_id: int
    student_id: int


class CaseCreate(CaseBase):
    pass


class Case(CaseBase):
    id: int

    class Config:
        orm_mode = True


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


class UserBase(BaseModel):
    username: str
    #first_name: str
    #last_name: str
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    roles: List[Role] = []
    caseloads: List[Caseload] = []

    class Config:
        orm_mode = True


class UserInDB(User):
    hashed_password: str


class Token(BaseModel):
    access_token: str
    token_type: str
    user: User


class TokenData(BaseModel):
    username: Optional[str] = None
