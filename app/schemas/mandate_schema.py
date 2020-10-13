from pydantic import BaseModel


class MandateBase(BaseModel):
    service: str
    group_size: int
    duration: int
    periodicity: str
    frequency: int
    interval: int

    class Config:
        orm_mode = True


class MandateCreate(MandateBase):
    iep_id: int


class Mandate(MandateBase):
    id: int


class MandateThin(MandateBase):
    iep_id: int
    id: int
