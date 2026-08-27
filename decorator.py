import os
from functools import wraps
from typing import Callable


def require_json_file(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        if not os.path.exists(self.js_name):
            return None

        return func(self, *args, **kwargs)

    return wrapper