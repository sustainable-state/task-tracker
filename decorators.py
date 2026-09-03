from typing import Callable
from functools import wraps
from utils import get_tasks_id
from exceptions import (
    TaskNotFoundError, 
    IntegerArgumentError, 
    ArgumentCountError
)


def argument_count(*counts: int):
    def decorator(func: Callable):
        @wraps(func)
        def wrapper(self):
            if len(self.args) not in counts:
                allowed = " or ".join(map(str, counts))

                raise ArgumentCountError(
                    f"Error: {self.command!r} requires "
                    f"{allowed} argument(s), "
                    f"but {len(self.args)} were provided."
                )

            return func(self)
        return wrapper
    return decorator


def parse_integer_argument(func: Callable):
    @wraps(func)
    def wrapper(self):
        raw_task_id = self.args[0]

        try:
            task_id = int(raw_task_id)
        except ValueError as error:
            raise IntegerArgumentError(
                f"Error: {self.command!r} requires integer argument "
                f"but {raw_task_id!r} were provided."
            ) from error
        
        self.args = (task_id, *self.args[1:])
        
        return func(self)
    return wrapper


def validate_task_id(func: Callable):
    @wraps(func)
    def wrapper(self, *args):
        task_id = args[0]
        tasks = self.js_manager.read()

        if task_id not in get_tasks_id(tasks):
            raise TaskNotFoundError(f"Error: task id {task_id!r} does not exist.") 
        
        return func(self, *args, tasks=tasks)
    return wrapper

            
