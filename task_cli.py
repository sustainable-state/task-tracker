import sys
from task_service import TaskService
from utils import extract_rest

class CLI:
    def __init__(self, command: str, *args: str, js_name: str = "tasks.json") -> None:
        self.json_name = js_name
        self.command = command
        self.args = args
        
        self.task_service = TaskService(js_name)

        self.operator = {
            "add": self.add_task,
            "update": self.update_task
        }

    
    def execute_opertion(self) -> None:
        if self.command in self.operator:
            self.operator[self.command]()

    
    def add_task(self) -> None:
        self.task_service.add(*self.args)

    
    def update_task(self) -> None:
        id, description = self.args
        self.task_service.update(int(id), description)




if __name__ == "__main__":
    cli = CLI(*extract_rest(*sys.argv))
    cli.execute_opertion()