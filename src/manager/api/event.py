from typing import List

from sqlalchemy import select, update
from sqlalchemy.orm import Session

from src.manager.api.user import get_user
from src.manager.database.models import Event as EventModel
from src.manager.database.schemas.event import EventCreate


# TODO write events to database
def create_event(db: Session, new_event: EventCreate) -> EventModel:
    db_event = EventModel(**new_event.dict())

    db.add(db_event)
    db.commit()
    db.refresh(db_event)

    return db_event


# TODO add error handling messages to this function
def get_event(db: Session, event_id: int) -> EventModel | None:

    db_event = db.get(EventModel, event_id)

    if db_event.is_deleted:
        return db_event
    
    print("Error message about Event being deleted")


def get_events(db: Session) -> List[EventModel, None]:
    return db.scalars(select(EventModel).where(EventModel.is_deleted == False)).all()


# REDO this function to check for error handling
def update_event_details(db: Session, event_id: int, new_details: str):
    return db.execute(
        update(EventModel).where(EventModel.id == event_id).values(details=new_details)
    )


# TODO update existing event title
# REDO this function to check for error handling
def update_event_title(db: Session, event_id: int, new_title: str):
    return db.execute(
        update(EventModel).where(EventModel.id == event_id).values(title=new_title)
    )


# FIXME update existing guest. Add proper error handling
def update_event_guest(db: Session, event_id: int, new_guest: str):
    db_event = get_event(db=db, event_id=event_id)

    if new_guest in db_event.guest:
        print("Guest already on timeline")
        return

    db_event.guest += [new_guest]
    db.commit()


# FIXME update existing event host. Add proper error handling
def update_event_host(db: Session, host_id: int, event_id: int):
    db_host = get_user(db=db, user_id=host_id)
    db_event = get_event(db=db, event_id=event_id)

    if host_id in list(db_event.host):
        print("Host already on Event")
        return

    db_event.host += [db_host]
    db.commit()


# TODO add error handling messages to this function
def delete_event(db: Session, event_id: int):
    db_event = get_event(db=db, event_id=event_id)

    if db_event.is_deleted:
        db_event.is_deleted = True
    else:
        print("Some Error message about event already being deleted")
    db.commit()
