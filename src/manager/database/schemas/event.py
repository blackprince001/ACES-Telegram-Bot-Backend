from pydantic import BaseModel
from typing import List
from datetime import datetime as date

from src.manager.database.models import Event as EventModel


class EventBase(BaseModel):
    pass


class EventCreate(EventBase):
    host: List[EventModel]
    details: str
    guest: list = []
    dt_created: date


class Event(EventBase):
    class Config:
        orm_mode = True
        arbitrary_types_allowed = True
