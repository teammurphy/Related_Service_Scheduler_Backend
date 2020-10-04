from typing import List

import crud.case
import models
from database import get_db
from fastapi import APIRouter, Depends, HTTPException
from schemas import case_schema, caseload_schema, user_schema
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/case", tags=["case"])
def create_case(case: case_schema.CaseCreate, db: Session = Depends(get_db)):
    return crud.case.create_case(db=db, case=case)


@router.get("/cases", response_model=List[case_schema.Case], tags=["case"])
def read_all_cases(db: Session = Depends(get_db)):
    cases = crud.case.get_all_cases(db)
    if not cases:
        raise HTTPException(status_code=404, detail="cases not found")
    return cases


@router.get("/case/{case_id}", response_model=case_schema.Case, tags=["case"])
def read_case(case_id: int, db: Session = Depends(get_db)):
    case = crud.case.get_case(db, case_id=case_id)
    if case is None:
        raise HTTPException(status_code=404, detail="Case not found")
    return case


@router.get("/cases/byUserId/{user_id}", response_model=user_schema.User, tags=["case"])
def read_cases_by_user(user_id: int, db: Session = Depends(get_db)):
    user = crud.case.get_user(db, user_id=user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user.cases


@router.put("/case/{case_id}", tags=["case"])
def updated_case(updated_case: case_schema.CaseCreate, case_id: int, db: Session = Depends(get_db)):
    updated = crud.case.update_case(
        db=db, case_id=case_id, updated_case=updated_case)
    if update is False:
        raise HTTPException(status_code=404, detail="case not found")
    return case_id


@router.delete("/case/{case_id}", tags=["case"])
def delete_case(case_id: int, db: Session = Depends(get_db)):
    deleted = crud.case.delete_case(db=db, case_id=case_id)
    if deleted is False:
        raise HTTPException(status_code=404, detail="Case not found")
    return case_id
