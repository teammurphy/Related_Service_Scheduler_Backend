import logging

import crud.student
import crud.user
from authentication import get_current_active_user
from database import get_db
from fastapi import APIRouter, Depends, HTTPException, Security, status
from schemas import user_schema
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/provider/caseloads", tags=["provider"])
async def get_provider_caseload(current_user: user_schema.User = Security(get_current_active_user, scopes=["me", "provider"])):
    return current_user.caseloads


@router.get("/provider/students/school/{school_id}", tags=["provider"])
async def get_students_by_school(school_id: str, current_user: user_schema.User = Security(get_current_active_user, scopes=["me", "provider"]), db: Session = Depends(get_db)):
    schools = []

    for role in current_user.roles:
        if role.name == 'provider':
            schools.append(role.school)
    if school_id not in schools:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not enough permissions"
        )
    return (crud.student.get_students_by_school_id(db, school_id))
