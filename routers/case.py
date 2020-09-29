from typing import List

import crud
import models
import schemas
from database import get_db
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/case", tags=["case"])
def create_case(case: schemas.CaseCreate, db: Session = Depends(get_db)):
    return crud.create_case(db=db, case=case)


@router.get("/cases", response_model=List[schemas.Case], tags=["case"])
def read_all_cases(db: Session = Depends(get_db)):
    cases = crud.get_all_cases(db)
    if not cases:
        raise HTTPException(status_code=404, detail="cases not found")
    return cases


@router.get("/case/{case_id}", response_model=schemas.Case, tags=["case"])
def read_case(case_id: int, db: Session = Depends(get_db)):
    case = crud.get_case(db, case_id=case_id)
    if case is None:
        raise HTTPException(status_code=404, detail="Case not found")
    return case


@router.get("/cases/byUserId/{user_id}", response_model=schemas.User, tags=["case"])
def read_cases_by_user(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id=user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user.cases


@router.put("/case/{case_id}", tags=["case"])
def updated_case(updated_case: schemas.CaseCreate, case_id: int, db: Session = Depends(get_db)):
    updated = crud.update_case(
        db=db, case_id=case_id, updated_case=updated_case)
    if update is False:
        raise HTTPException(status_code=404, detail="case not found")
    return case_id


@router.delete("/case/{case_id}", tags=["case"])
def delete_case(case_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_case(db=db, case_id=case_id)
    if deleted is False:
        raise HTTPException(status_code=404, detail="Case not found")
    return case_id
