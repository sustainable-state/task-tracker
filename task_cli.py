import sys
from task_service import TaskService
from utils import extract_rest, argument_count


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
            "mark-in-progress": self.mark_task,
            "mark-done": self.mark_task,
            "help": self.help

        }

    
    def execute_operation(self) -> None:
        if self.command in self.operator:
            self.operator[self.command]()
        else:
            print(
                f"entered action do not support {self.command!r}. "
                "Otherwise enter 'help' to see supported actions"
            )

    
    @argument_count(1)
    def add_task(self) -> None:
        description = self.args[0]
        self.task_service.add(description)


    @argument_count(2)
    def update_task(self) -> None:
        task_id, description = self.args
        self.task_service.update(int(task_id), description)

    
    @argument_count(1)
    def delete_task(self) -> None:
        task_id = self.args[0]
        self.task_service.delete(int(task_id))

    
    @argument_count(1)
    def mark_task(self) -> None:
        _, task_status = self.command.split("-", 1)

        task_id = self.args[0]

        self.task_service.mark(
            task_status=task_status,
            task_id=int(task_id)
        )

    
    @argument_count(0)
    def help(self) -> None:
        print("Supported actions")

        for action in self.operator:
            print(action)

        print("read 'README.md' to use actions properly")


if __name__ == "__main__":
    cli = CLI(*extract_rest(*sys.argv))
    cli.execute_operation()