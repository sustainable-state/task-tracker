from datetime import datetime
from dataclasses import dataclass


TASK_STATUSES = ("todo", "in-progress", "done")


@dataclass
class Task:
    task_id: int
    description: str
    status: str
    created_at: str
    updated_at: str | None = None


def extract_rest(*args):
    _, *rest = args
    return rest


def current_datetime() -> str:
    return datetime.now().strftime("%d-%m-%YT%H:%M")


def get_tasks_id(tasks: list[Task]):
    if not tasks:
        return ()
    
    return tuple(row.task_id for row in tasks)


def generate_id(tasks_id: tuple[int, ...]) -> int:
    if not tasks_id:
        return 1

    return max(tasks_id) + 1