import logging
from typing import List

import crud
import models
import schemas
from database import engine, get_db
from fastapi import Depends, FastAPI, HTTPException
from routers import (case, caseload, goal, iep, mandate, roles, school,
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


@app.get("/")
async def root():
    return {"message": "Hello World"}
