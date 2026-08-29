from json_manager import JsonManager
from utils import (
    Task, 
    current_datetime, 
    generate_id, 
    get_tasks_id
)


class TaskService:
    def __init__(self, file_name: str):
        self.file_name = file_name
        self.js_manager = JsonManager(file_name)
        

    def add(self, description: str) -> None:
        tasks = self.js_manager.read()

        if tasks is None:
            tasks = []
        
        tasks.append(
            Task(
                task_id=generate_id(tasks=tasks), 
                description=description, 
                status="todo",
                createdAt=current_datetime(),
                updatedAt=None
            )
        )

        self.js_manager.save(tasks=tasks)

    
    def update(self, task_id: int, description: str) -> None:
        tasks = self.js_manager.read()

        if tasks is None:
            return

        if task_id in get_tasks_id(tasks):
            for task in tasks:
                if task.task_id == task_id:
                    task.description = description
                    task.updatedAt = current_datetime()
                    break

            self.js_manager.save(tasks=tasks)

    
    def delete(self, task_id: int) -> None:
        tasks = [task for task in self.js_manager.read() if task.task_id != task_id]

        self.js_manager.save(tasks=tasks)


