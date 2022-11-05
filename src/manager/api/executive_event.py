from sqlalchemy import select
from sqlalchemy.orm import Session
from src.manager.database.schemas.executive_event import ExecutiveEventCreate
from src.manager.database.models import ExecutiveEvent as ExecutiveEventModel
from typing import List


def create_executive_event(
    db: Session, new_executive_event: ExecutiveEventCreate
) -> ExecutiveEventModel:
    db_e_event = ExecutiveEventModel(**new_executive_event.dict())

    db.add(db_e_event)
    db.commit()
    db.refresh(db_e_event)

    return db_e_event


def get_executive_event(
    db: Session, user_id: int, event_id: int
) -> ExecutiveEventModel:
    return db.scalar(
        select(ExecutiveEventModel)
        .where(ExecutiveEventModel.event_id == event_id)
        .where(ExecutiveEventModel.user_id == user_id)
    )


def get_executive_events(db: Session) -> List[ExecutiveEventModel]:
    return db.scalars(select(ExecutiveEventModel)).all()
