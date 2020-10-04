from typing import List

import crud.goal
import models
from database import get_db
from fastapi import APIRouter, Depends, HTTPException
from schemas import goal_schema
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/goal", tags=["goal"])
def create_goal(goal: goal_schema.GoalCreate, db: Session = Depends(get_db)):
    return crud.goal.create_goal(db=db, goal=goal)


@router.get("/goal/{goal_id}", response_model=goal_schema.Goal, tags=["goal"])
def read_goal(goal_id: int, db: Session = Depends(get_db)):
    goal = crud.goal.get_goal(db, goal_id=goal_id)
    if goal is None:
        raise HTTPException(status_code=404, detail="Goal not found")
    return goal


@router.put("/goal/{goal_id}", tags=["goal"])
def update_goal(updated_goal: goal_schema.GoalCreate, goal_id: int, db: Session = Depends(get_db)):
    updated = crud.goal.update_goal(
        db=db, goal_id=goal_id, updated_goal=updated_goal)
    if update is False:
        raise HTTPException(status_code=404, detail="Goal not found")
    return goal_id


@router.delete("/goal/{goal_id}", tags=["goal"])
def delete_goal(goal_id: int, db: Session = Depends(get_db)):
    deleted = crud.goal.delete_goal(db=db, goal_id=goal_id)
    if deleted is False:
        raise HTTPException(status_code=404, detail="Goal not found")
    return goal_id
