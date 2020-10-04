import logging
from datetime import datetime, timedelta

import authentication
import crud.user
import schemas
from database import get_db
from fastapi import APIRouter, Depends, HTTPException, Security, status
from fastapi.security import (OAuth2PasswordBearer, OAuth2PasswordRequestForm,
                              SecurityScopes)
from jose import JWTError, jwt
from passlib.context import CryptContext
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/token", response_model=schemas.Token, tags=['auth'])
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authentication.authenticate_user(
        db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(
        minutes=authentication.ACCESS_TOKEN_EXPIRE_MINUTES)
    scopes = authentication.get_scopes_from_db(user)
    access_token = authentication.create_access_token(
        data={"sub": user.username, "scopes": scopes},
        expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer", "user": user}


@router.get("/users/me", tags=["auth"])
async def read_users_me(current_user: schemas.User = Depends(authentication.get_current_user)):
    return current_user
