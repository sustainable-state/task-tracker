from datetime import datetime
from utils import current_datetime, generate_id, get_tasks_id
from json_manager import JsonManager


class TaskService:
    def __init__(self, file_name: str):
        self.file_name = file_name
        self.js_manager = JsonManager(file_name)
        

    def add(self, description: str) -> None:
        tasks = self.js_manager.read()
        date = current_datetime()
        task_id = generate_id(tasks=tasks)

        if tasks is None:
            tasks = []
        
        tasks.append(
            self.generate_task(
                task_id=task_id, 
                description=description, 
                status="todo",
                created_at=date
            )
        )

        self.js_manager.save(tasks=tasks)

    
    def update(self, task_id: int, description: str) -> None:
        tasks = self.js_manager.read()

        if tasks is None:
            return

        if task_id in get_tasks_id(tasks):
            for task in tasks:
                if task["id"] == task_id:
                    task["description"] = description
                    task["updatedAt"] = current_datetime()
                    break

        self.js_manager.save(tasks=tasks)

    
    def delete(self, task_id: int) -> None:
        tasks = [row for row in self.js_manager.read() if row["id"] != task_id]

        self.js_manager.save(tasks=tasks)
    

    def generate_task(
            self,
            task_id: int, 
            description: str, 
            status: str, 
            created_at: str,
            updated_at: str | None = None
        ) -> dict:

        return {
            "id": task_id,
            "description": description,
            "status": status,
            "createdAt": created_at,
            "updatedAt": updated_at
        }


