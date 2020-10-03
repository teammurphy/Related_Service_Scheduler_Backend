import logging
from functools import lru_cache
from typing import List

import config
import crud
import models
import schemas
from database import engine, get_db
from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
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


@lru_cache()
def get_settings():
    return config.Settings()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
