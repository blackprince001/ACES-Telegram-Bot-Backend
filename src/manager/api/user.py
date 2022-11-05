from sqlalchemy import update, select
from sqlalchemy.orm import Session
from src.manager.database.schemas.user import UserCreate
from src.manager.database.models import User as UserModel
from typing import List


def create_user(db: Session, new_user: UserCreate) -> UserModel:
    db_user = UserModel(**new_user.dict())

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


def get_user(db: Session, user_id: int) -> UserModel | None:
    return db.get(UserModel, user_id)


def get_executive(db: Session, user_id: int) -> UserModel | None:
    return db.scalar(select(UserModel).where(UserModel.is_executive == True))


def get_users(db: Session) -> List[UserModel]:
    return db.scalars(select(UserModel)).all()


def get_executives(db: Session) -> List[UserModel]:
    return db.scalars(select(UserModel).where(UserModel.is_executive == True)).all()


def update_user_name(db: Session, user_id: int, new_name: str):
    db_user = get_user(db=db, user_id=user_id)

    db_user.name = new_name
    db.commit()

    return db_user


def update_user_bio(db: Session, user_id: int, new_bio: str):
    db_user = get_user(db=db, user_id=user_id)

    db_user.bio = new_bio
    db.commit()

    return db_user


# FIXME add proper error handling for this method
def update_executive_status(db: Session, user_id: int):
    db_user = get_user(db=db, user_id=user_id)

    if db_user.is_executive:
        db_user.is_executive = False

    print("add some error handling if the person is not already an executive")
    db.commit()

    return db_user
