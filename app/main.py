import logging
from functools import lru_cache
from typing import List

import config
import custom_exceptions
import models
from database import engine, get_db
from fastapi import Depends, FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from routers import (admin, auth, case, caseload, event, goal, iep, mandate,
                     providers, roles, school, student, supervisors, users)
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
app.include_router(admin.router)
app.include_router(providers.router)
app.include_router(supervisors.router)
app.include_router(event.router)


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


@app.exception_handler(custom_exceptions.InvaldEntryException)
async def wrong_county_exception_handler(request: Request, exc: custom_exceptions.InvaldEntryException):
    return JSONResponse(
        status_code=418,
        content={
            "message": f"Invlaid entry '{exc.entered}' not in allowed {exc.allowed}"},

    )
