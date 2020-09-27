from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel


class GoalBase(BaseModel):
    goal: str
    criteria: str
    method: str
    schedule: str


class Goal(GoalBase):
    id: int
    iep_id: int


class MandateBase(BaseModel):
    service: str
    group_size: int
    duration: int
    periodicity: str
    frequency: int
    interval: int


class Mandate(MandateBase):
    id: int
    iep_id: int


class IepBase(BaseModel):
    start_date: datetime
    end_date: datetime


class Iep(IepBase):
    id: int
    student_id: int
    mandates: List[Mandate] = []
    goals: List[Goal] = []

    class Config:
        orm_mode = True


class StudentBase(BaseModel):
    first_name: str
    last_name: str
    osis: str
    birthdate: datetime
    grade: str


class Student(StudentBase):
    id: int
    school_id: int
    ieps: List[Iep] = []

    class Config:
        orm_mode = True


class SchoolBase(BaseModel):
    district: str
    country: str
    name: str


class School(SchoolBase):
    id: str
    students: List[Student] = []

    class Config:
        orm_mode = True


class RoleBase(BaseModel):
    user_role: str


class RoleCreate(RoleBase):
    pass


class Role(RoleBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True


class CaseBase(BaseModel):
    pass


class Case(CaseBase):
    id: int
    caseload_id: int
    student_id: int

    class Config:
        orm_mode = True


class CaseloadBase(BaseModel):
    title: str
    service: str


class Caseload(CaseloadBase):
    id: int
    user_id: int
    cases: List[Case] = []

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    username: str
    first_name: str
    last_name: str
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    role: List[Role] = []
    caseloads: List[Caseload] = []

    class Config:
        orm_mode = True
