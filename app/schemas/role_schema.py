from datetime import date, datetime
from typing import List, Optional

from pydantic import BaseModel


class RoleBase(BaseModel):
    name: str
    school: str
    district: str
    county: str
    service: str


class RoleCreate(RoleBase):
    user_id: int


class Role(RoleBase):
    id: int

    class Config:
        orm_mode = True


class RoleAddToUser(RoleBase):
    pass
