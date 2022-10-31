from pydantic import BaseModel
from datetime import datetime as date


class IssueBase(BaseModel):
    statement: str
    dt_created: date


class IssueCreate(IssueBase):
    class Config:
        orm_mode = True
        arbitrary_types_allowed = True


class ResolvedIssueBase(IssueBase):
    pass


class ResolvedIssueCreate(ResolvedIssueBase):
    dt_resolved: date
    is_resolved: bool = True

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True
