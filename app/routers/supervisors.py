import logging
from typing import List

import crud.user
from authentication import get_current_active_user
from database import get_db
from fastapi import APIRouter, Depends, HTTPException, Security, status
from schemas import user_schema
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/supervisor/providers/{district}/{service}", tags=["supervisor"], response_model=List[user_schema.UserThin])
async def get_providers_by_district(district: str, service: str, current_user: user_schema.User = Security(get_current_active_user, scopes=["me", "supervisor"]), db: Session = Depends(get_db)):
    districts = []
    for role in current_user.roles:
        if role.name == 'supervisor' and role.service == service:
            districts.append(role.district)
    if district not in districts:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not enough permissions"
        )

    logging.info(crud.user.get_providers_by_district_and_service(
        db, district, service))

    return (crud.user.get_providers_by_district_and_service(db, district, service))
