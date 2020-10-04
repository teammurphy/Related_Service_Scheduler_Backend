from typing import List, Optional

from pydantic import BaseModel

from .caseload_schema import Caseload
from .role_schema import Role


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
    disabled: bool

    class Config:
        orm_mode = True


class UserResponse(UserBase):
    id: int
    roles: List[Role] = []
    disabled: bool

    class Config:
        orm_mode = True


class UserInDB(User):
    hashed_password: str
