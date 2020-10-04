from typing import List, Optional

from pydantic import BaseModel

from .user_schema import UserResponse


class Token(BaseModel):
    access_token: str
    token_type: str
    user: UserResponse


class TokenData(BaseModel):
    username: Optional[str] = None
    scopes: List[str] = []
