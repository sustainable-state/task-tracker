from datetime import datetime
from dataclasses import dataclass


@dataclass
class Task:
    task_id: int
    description: str
    status: str
    createdAt: str
    updatedAt: str | None



def extract_rest(*args):
    _, *rest = args
    return rest


def current_datetime() -> str:
    return datetime.now().strftime("%d-%m-%YT%H:%M")


def generate_id(tasks: list[Task] | None) -> int:
    try:
        return max(get_tasks_id(tasks)) + 1
    except ValueError:
        return 1


def get_tasks_id(tasks: list[Task] | None) -> tuple[int, ...]:
    if not tasks:
        return ()

    return tuple(task.task_id for task in tasks)