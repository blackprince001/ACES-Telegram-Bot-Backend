from pydantic import BaseModel
from typing import List
from datetime import datetime as date

from src.manager.database.models import User as UserModel


class EventBase(BaseModel):
    pass


class EventCreate(EventBase):
    host: List[UserModel]
    title: str
    details: str
    guest: list = []
    dt_created: date
    is_cancelled: bool
    is_deleted: bool


class Event(EventBase):
    class Config:
        orm_mode = True
        arbitrary_types_allowed = True
    