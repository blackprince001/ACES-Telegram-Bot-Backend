from typing import List

from sqlalchemy import select, update
from sqlalchemy.orm import Session

from user import get_user
from database.models import Event as EventModel
from schemas.event import EventCreate

from error_handling.errors import (
    HostNotFound, EventAlreadyExist, HostAlreadyExist, EventNotFound
)


def create_event(
    db: Session, new_event: EventCreate, host_ids: List[int]
) -> EventModel:
    db_event = EventModel(**new_event.dict())
    hosts = set()
    for host_id in host_ids:
        host = get_user(db=db, user_id=host_id)
        if host is None:
            raise HostNotFound(status_code=404, detail=f"No user with id={host_id}")
        hosts.add(host)
    for host in hosts:
        db_event.host.append(host)
    db.add(db_event)
    db.commit()
    db.refresh(db_event)

    return db_event


def get_event(db: Session, event_id: int) -> EventModel | None:
    db_event = db.get(EventModel, event_id)
    if db_event.is_deleted:
        return db_event
    else:
        raise EventNotFound(
            status_code=404, detail="Event not found, might be deleted!"
        )


def get_events(db: Session) -> List[EventModel, None]:
    return db.scalars(select(EventModel).where(EventModel.is_deleted is False)).all()


def update_event_details(db: Session, event_id: int, new_details: str):
    return db.execute(
        update(EventModel).where(EventModel.id == event_id).values(details=new_details)
    )


def update_event_title(db: Session, event_id: int, new_title: str):
    return db.execute(
        update(EventModel).where(EventModel.id == event_id).values(title=new_title)
    )


def update_event_guest(db: Session, event_id: int, new_guest: str):
    db_event = get_event(db=db, event_id=event_id)
    if new_guest in db_event.guest:
        raise EventAlreadyExist(
            status_code=409, detail=f"Event with id {event_id} already exist!")
    db_event.guest += [new_guest]
    db.commit()


def update_event_host(db: Session, host_id: int, event_id: int):
    db_host = get_user(db=db, user_id=host_id)
    db_event = get_event(db=db, event_id=event_id)

    if host_id in list(db_event.host):
        raise HostAlreadyExist(
            status_code=409, detail=f"Host with id {host_id} is already on timeline!")
    db_event.host += [db_host]
    db.commit()


def delete_event(db: Session, event_id: int):
    db_event = get_event(db=db, event_id=event_id)
    if db_event.is_deleted:
        db_event.is_deleted = True
    else:
        raise EventNotFound(
            status_code=404, detail="Event is not found, might already been deleted!")
    db.commit()
