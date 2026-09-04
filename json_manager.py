import json
import os

from utils import Task
from exceptions import InvalidJsonError, InvalidTaskStructureError


class JsonManager:
    def __init__(self, file_name: str) -> None:
        self.file_name = file_name
        

    def save(self, tasks: list[Task]) -> None:
        with open(self.file_name, "w", encoding="utf-8") as file:
            json.dump(
                [self.dict_format(row) for row in tasks], 
                file, 
                indent=4,
                ensure_ascii=False
            )
    

    def read(self) -> list[Task]:
        if not os.path.exists(self.file_name):
            return []

        try:
            with open(self.file_name, "r", encoding="utf-8") as file:
                data = json.load(file)
            
            if not isinstance(data, list):
                raise InvalidTaskStructureError(
                    f"{self.file_name!r} must contain a list of tasks."
                )

            return [self.task_format(row) for row in data]

        except json.JSONDecodeError as error:
            raise InvalidJsonError(
                f"{self.file_name!r} contains invalid JSON data."
            ) from error

        except (KeyError, TypeError) as error:
            raise InvalidTaskStructureError(
                f"{self.file_name!r} does not match "
                "the expected task structure."
            ) from error
        
        
    @staticmethod
    def dict_format(task: Task) -> dict[str, object]:

        return {
            "id": task.task_id,
            "description": task.description,
            "status": task.status,
            "createdAt": task.created_at,
            "updatedAt": task.updated_at
        }
    

    @staticmethod
    def task_format(dict_task: dict) -> Task:
        return Task(
            task_id=dict_task["id"],
            description=dict_task["description"],
            status=dict_task["status"],
            created_at=dict_task["createdAt"],
            updated_at=dict_task["updatedAt"],
        )

