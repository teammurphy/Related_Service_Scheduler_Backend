import logging
from typing import List

import crud
import models
import schemas
from database import engine, get_db
from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from routers import (auth, case, caseload, goal, iep, mandate, roles, school,
                     student, users)
from sqlalchemy.orm import Session

logging.basicConfig(filename='main.log',
                    format='[%(filename)s:%(lineno)d] %(message)s', level=logging.DEBUG)
logging.warning("New Run Starts Here")

models.Base.metadata.create_all(bind=engine)


app = FastAPI()
app.include_router(users.router)
app.include_router(roles.router)
app.include_router(student.router)
app.include_router(school.router)
app.include_router(iep.router)
app.include_router(mandate.router)
app.include_router(goal.router)
app.include_router(case.router)
app.include_router(caseload.router)
app.include_router(auth.router)


'''

def fake_decode_token(token):
    db = next(get_db())
    user = crud.get_user_by_username(db, token)
    logging.info(user)
    return user


async def get_current_user(token: str = Depends(oauth2_scheme)):
    user = fake_decode_token(token=token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user



'''
'''
@ app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = crud.get_user_by_username(db, form_data.username)
    logging.info(db)
    if user is None:
        raise HTTPException(
            status_code=400, detail="Incorrect username or password")
    hashed_password = form_data.password
    if not hashed_password == user.hashed_password:
        raise HTTPException(
            status_code=400, detail="Incorrect username or password")

    return {"access_token": user.username, "token_type": "bearer"}
'''

'''
@ app.get("/items/")
async def read_items(token: str = Depends(oauth2_scheme)):
    return {"token": token}

'''
