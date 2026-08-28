from datetime import datetime


def extract_rest(*args):
    _, *other = args
    return other


def current_datetime() -> str:
    return datetime.now().strftime("%d-%m-%YT%H:%M")


def generate_id(tasks: list[dict] | list | None) -> int:
    if tasks is None or not bool(tasks):
        return 1
    
    return max(get_tasks_id(tasks)) + 1


def get_tasks_id(tasks: list[dict] | list | None) -> tuple[int, ...]:
    if tasks is None or not bool(tasks):
        return ()
    
    return tuple((task["id"] for task in tasks))
    