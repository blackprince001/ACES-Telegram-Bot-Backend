from pydantic import BaseModel


class UserBase(BaseModel):
    pass


class UserCreate(UserBase):
    name: str
    bio: str


class User(UserBase):
    class Config:
        orm_mode = True
        arbitrary_types_allowed = True


class ExecutiveBase(UserBase):
    pass


class ExecutiveCreate(UserCreate):
    is_executive: bool = True


class Executive(ExecutiveBase):
    class Config:
        orm_mode = True
        arbitrary_types_allowed = True
