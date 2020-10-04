from pydantic import BaseModel


class MandateBase(BaseModel):
    service: str
    group_size: int
    duration: int
    periodicity: str
    frequency: int
    interval: int


class MandateCreate(MandateBase):
    iep_id: int


class Mandate(MandateBase):
    id: int
