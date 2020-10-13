from pydantic import BaseModel


class GoalBase(BaseModel):
    goal: str
    criteria: str
    method: str
    schedule: str

    class Config:
        orm_mode = True


class GoalCreate(GoalBase):
    iep_id: int


class Goal(GoalBase):
    id: int
