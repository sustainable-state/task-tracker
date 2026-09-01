from typing import Callable
from functools import wraps


def argument_count(count: int):
    def decorator(func: Callable):
        @wraps(func)
        def wrapper(self):
            if count != len(self.args):
                print(
                    f"Error: {self.command!r} requires {count} argument(s), "
                    f"but {len(self.args)} were provided."
                )
                return 

            return func(self)
        return wrapper
    return decorator


def integer_argument(func: Callable):
    @wraps(func)
    def wrapper(self):

        try:
            task_id = self.args[0]
            int(task_id)
        except ValueError:
            print(
                f"Error: {self.command!r} requires integer argument "
                f"but {task_id!r} were provided."
                )
            return 
        else:
            return func(self)
        
    return wrapper