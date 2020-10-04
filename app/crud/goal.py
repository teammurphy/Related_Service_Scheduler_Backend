import logging

import models
from schemas import goal_schema
from sqlalchemy.orm import Session


def get_goal(db: Session, goal_id: int):
    return db.query(models.Goal).filter(models.Goal.id == goal_id).first()


def create_goal(db: Session, goal: goal_schema.GoalCreate):
    db_goal = models.Goal()
    [setattr(db_goal, i[0], i[1]) for i in goal]

    db.add(db_goal)
    db.commit()
    db.refresh(db_goal)
    return db_goal


def delete_goal(db: Session, goal_id: int):
    db_goal = get_goal(db, goal_id)
    if db_goal:
        db.delete(db_goal)
        db.commit()
        return True
    else:
        return False


def update_goal(db: Session, goal_id: int, updated_goal: goal_schema.GoalCreate):
    db_goal = get_goal(db, goal_id)
    if db_goal is None:
        return False
    return update_object(db, db_goal, updated_goal)


def update_goal(db: Session, goal_id: int, updated_goal: goal_schema.GoalCreate):
    db_goal = get_goal(db, goal_id)
    if db_goal is None:
        return False

    [setattr(db_goal, i[0], i[1]) for i in updated_goal]
    db.commit()
    db.refresh(db_goal)
    return True
