import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import datetime

from manager.database.models import Base
from manager.database.schemas.event import EventCreate
from manager.database.schemas.user import UserCreate
from manager.database.schemas.issues import IssueCreate


@pytest.fixture(scope="session")
def engine():
    return create_engine(url="sqlite+pysqlite:///:memory:", future=True)


@pytest.fixture(scope="session")
def issue():
    now = datetime.datetime.now()
    return IssueCreate(
        statement="We could not resolve the number of chairs in auditorium",
        dt_created=now,
    )

@pytest.fixure(scope="session")
def user():
    return UserCreate(
        name="blackprince", bio="the Ego is an illusion"
    )


@pytest.fixture(scope="session")
def event(user):
    now = datetime.datetime.now()
    return EventCreate(
        host=[user], title="creating awareness for mental health",
        guest=["Kwaku Bonsam"], dt_created=now, is_cancelled=False
    )


@pytest.fixture
def db(engine):
    with Session(engine) as session:
        Base.metadata.create_all(bind=engine)
        yield session