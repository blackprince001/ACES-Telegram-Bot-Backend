from pydantic import ArbitraryTypeError, BaseModel


class UserBase(BaseModel):
    pass


class UserCreate(UserBase):
    name: str
    bio: str

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True


class ExecutiveBase(UserBase):
    pass


class ExecutiveCreate(ExecutiveBase):
    is_executive: bool = True


class Executive(ExecutiveBase):
    class Config:
        orm_mode = True
        arbitrary_types_allowed = True
