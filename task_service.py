from json_manager import JsonManager
from decorators import validate_task_id
from utils import (
    Task, 
    current_datetime, 
    generate_id,
    get_tasks_id 
)


class TaskService:
    def __init__(self, file_name: str):
        self.js_manager = JsonManager(file_name)
        

    def add(self, description: str) -> None:
        tasks = self.js_manager.read()
        
        tasks.append(
            Task(
                task_id=generate_id(get_tasks_id(tasks)), 
                description=description, 
                status="todo",
                created_at=current_datetime(),
            )
        )

        self.js_manager.save(tasks=tasks)


    @validate_task_id
    def update(self, task_id: int, description: str, tasks: list[Task]) -> None:

        for task in tasks:
            if task.task_id == task_id:
                task.description = description
                task.updated_at = current_datetime()
                break

        self.js_manager.save(tasks=tasks)

    
    @validate_task_id
    def delete(self, task_id: int, tasks: list[Task]) -> None:
        tasks = [task for task in tasks if task.task_id != task_id]

        self.js_manager.save(tasks=tasks)


    @validate_task_id
    def mark(self, task_id: int, task_status: str, tasks: list[Task]) -> None:

        for task in tasks:
            if task.task_id == task_id:
                task.status = task_status
                task.updated_at = current_datetime()
                break

        self.js_manager.save(tasks=tasks)


