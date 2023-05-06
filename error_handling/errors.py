from fastapi import HTTPException

class UserError(HTTPException):
    pass


class UserNotFound(UserError):
    pass


class EventError(HTTPException):
    pass


class EventAlreadyExist(HTTPException):
    pass


class EventNotFound(EventError):
    pass


class EventHostNotGiven(EventError):
    pass


class HostNotFound(HTTPException):
    pass


class HostAlreadyExist(HTTPException):
    pass