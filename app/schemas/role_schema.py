from datetime import date, datetime
from typing import List, Optional

from pydantic import BaseModel


class RoleBase(BaseModel):
    name: str
    school_id: Optional[int]
    district: Optional[str]
    county: Optional[str]
    service: Optional[str]

    class Config:
        orm_mode = True


class RoleCreate(RoleBase):
    user_id: Optional[int]


class Role(RoleBase):
    id: int


class RoleAddToUser(RoleBase):
    pass


class RoleThin(RoleBase):
    user_id: int
    id: int
