from pydantic import BaseModel


class ExecutiveEventBase(BaseModel):
    pass


class ExecutiveEventCreate(ExecutiveEventBase):
    event_id: int
    host_id: int


class ExecutiveEvent:
    class Config:
        orm_mode = True
        arbitrary_types_allowed = True