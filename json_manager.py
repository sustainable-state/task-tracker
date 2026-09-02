import json
import os
from dataclasses import asdict

from utils import Task


class JsonManager:
    def __init__(self, file_name: str) -> None:
        self.file_name = file_name
        

    def save(self, tasks: list[Task]) -> None:
        with open(self.file_name, "w", encoding="utf-8") as file:
            json.dump(
                [asdict(row) for row in tasks], 
                file, 
                indent=4,
                ensure_ascii=False
            )
    

    def read(self) -> list[Task]:
        if not os.path.exists(self.file_name):
            return []

        try:
            with open(self.file_name, "r", encoding="utf-8") as file:

                return [Task(**row) for row in json.load(file)]
            
        except json.JSONDecodeError:
            return []


