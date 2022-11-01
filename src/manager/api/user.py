from sqlalchemy import select, update
from sqlalchemy.orm import Session
from manager.database.schemas.user import UserCreate as UserSchema
from src.manager.database.models import User as UserModel

# TODO write users to database
def create_user():
    pass


def get_user(db: Session, user_id: int) -> UserModel | None:
    return db.get(UserModel, user_id)


# TODO update existing user name
def update_user_name():
    pass


# TODO update existing user bio
def update_user_bio():
    pass
