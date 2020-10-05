import logging

import authentication
import crud.user
from authentication import get_current_active_user
from database import get_db
from fastapi import APIRouter, Depends, HTTPException, Security, status
from schemas import user_schema

router = APIRouter()


@router.get("/provider/caseloads", tags=["provider"])
async def get_provider_caseload(current_user: user_schema.User = Security(get_current_active_user, scopes=["me", "provider"])):
    return current_user.caseloads
