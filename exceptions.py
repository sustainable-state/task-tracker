class TaskTrackerError(Exception):
    ...


class InvalidJsonError(TaskTrackerError):
    ...


class InvalidTaskStatusError(TaskTrackerError):
    ...


class InvalidTaskStructureError(TaskTrackerError):
    ...


class TaskNotFoundError(TaskTrackerError):
    ...


class IntegerArgumentError(TaskTrackerError):
    ...


class ArgumentCountError(TaskTrackerError):
    ...


class InvalidDescriptionError(TaskTrackerError):
    ...