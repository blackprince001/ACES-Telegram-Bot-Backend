from sqlalchemy import select, update
from sqlalchemy.orm import Session
from src.manager.database.schemas.event import EventCreate as EventSchema
from src.manager.database.models import Event as EventModel

# TODO write events to database
def create_event():
    pass


def get_event(db: Session, event_id: int) -> EventModel | None:
    return db.get(EventModel, event_id)


def update_event_details(db: Session, event_id: int, new_details: str):
    return (
        db.query(EventModel)
        .get(EventModel == event_id)
        .update({EventModel.details: new_details}, synchronize_session=False)
    )


# TODO update existing event title
def update_event_title():
    pass


# TODO update existing guest
def update_event_guest():
    pass


# TODO update existing event host
def update_event_host():
    pass
