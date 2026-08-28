import sys
from task_service import TaskService
from utils import extract_rest

class CLI:
    def __init__(self, command: str, *args: str, file_name: str = "tasks.json") -> None:
        self.file_name = file_name
        self.command = command.lower()
        self.args = args
        
        self.task_service = TaskService(file_name)

        self.operator = {
            "add": self.add_task,
            "update": self.update_task,
            "delete": self.delete_task,
 #           "mark-in-progress": self.mark_in_progress_task
        }

    
    def execute_operation(self) -> None:
        if self.command in self.operator:
            self.operator[self.command]()

    
    def add_task(self) -> None:
        description = self.args[0]
        self.task_service.add(description)

    
    def update_task(self) -> None:
        task_id, description = self.args
        self.task_service.update(int(task_id), description)

    
    def delete_task(self) -> None:
        task_id = self.args[0]
        self.task_service.delete(int(task_id))

    
   # def mark_in_progress_task(self) -> None:
   #     task_id = self.args[0]
   #     self.task_service.mark_in_progress(int(task_id))


if __name__ == "__main__":
    cli = CLI(*extract_rest(*sys.argv))
    cli.execute_operation()