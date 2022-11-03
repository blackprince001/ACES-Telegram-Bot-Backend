from sqlalchemy import Column, String, DateTime, Integer, Boolean, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

BASE = declarative_base()


class ExecutiveEvent(BASE):
    __tablename__ = "executive_event"

    event_id = Column(ForeignKey("event.id"), primary_key=True)
    host_id = Column(ForeignKey("user.id"), primary_key=True)

    host = relationship("User", back_populates="executives", lazy="selectin")
    event = relationship("Event", back_populates="events", lazy="selectin")


class Event(BASE):
    __tablename__ = "event"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False, unique=False)
    details = Column(String, nullable=False, unique=False)
    guest = Column(String, nullable=True)
    host = Column(String, nullable=False, unique=True)
    dt_created = Column(DateTime, nullable=False)
    is_cancelled = Column(Boolean, nullable=False, default=False)

    events: list[ExecutiveEvent] = relationship(
        "ExecutiveEvent",
        back_populates="event",
        lazy="selectin",
    )


class User(BASE):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False, unique=True)
    bio = Column(String, nullable=True, unique=False)
    is_executive = Column(Boolean, nullable=True)

    executives: list[ExecutiveEvent] = relationship(
        "ExecutiveEvent",
        back_populates="user",
        lazy="selectin",
    )


""" 
Handle issue updates with `sqlalchemy.func` next time with `server_onupdate` and `on_update`
    date_created = Column(..., default=func.now())
    last_modified = Column(..., onupdate=func.now())
OR
    date_created = Column(..., server_default=func.now())
    last_modified = Column(..., server_onupdate=func.now())
"""
class Issues(BASE):
    __tablename__ = "issues"

    id = Column(Integer, primary_key=True, autoincrement=True)
    statement = Column(String, nullable=False, unique=False)
    dt_created = Column(DateTime, nullable=False)
    dt_resolved = Column(DateTime, nullable=True)
    is_resolved = Column(Boolean, nullable=False, default=False)
