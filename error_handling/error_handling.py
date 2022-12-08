class UserError(Exception):
    pass


class UserNotFound(UserError()):
    pass


class EventError(Exception):
    pass


class EventNotFound(EventError):
    pass


class EventHostNotGiven(EventError):
    pass
