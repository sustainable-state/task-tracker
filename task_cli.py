import sys
from task_service import TaskService
from utils import extract_rest, validate_description
from decorators import argument_count, parse_integer_argument
from exceptions import TaskTrackerError


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
            "help": self.help,
            "list": self.list_task,
        }

    
    def execute_operation(self) -> None:
        if self.command not in self.operator:
            print(
                f"Unsupported action: {self.command!r}. "
                "Use 'help' to see available actions."
            )
            return 
        
        try:
            self.operator[self.command]()
        except TaskTrackerError as error:
            print(error)


    @argument_count(0, 1)
    def list_task(self) -> None:
        status = self.args[0] if self.args else None
        tasks = self.task_service.listed(status)

        for task in tasks:
            print(f"{task.task_id}: {task.description}")
        
    
    @argument_count(1)
    def add_task(self) -> None:
        description = self.args[0]
        task_id = self.task_service.add(validate_description(description))
        print(f"Task added successfully (ID: {task_id})")


    @argument_count(2)
    @parse_integer_argument
    def update_task(self) -> None:
        task_id, description = self.args
        self.task_service.update(task_id, validate_description(description))
        print(f"Task updated successfully (ID: {task_id})")

    
    @argument_count(1)
    @parse_integer_argument
    def delete_task(self) -> None:
        task_id = self.args[0]
        self.task_service.delete(task_id)
        print(f"Task deleted successfully (ID: {task_id})")

    
    @argument_count(1)
    @parse_integer_argument
    def mark_task(self) -> None:
        task_id = self.args[0]
        _, task_status = self.command.split("-", 1)
        
        self.task_service.mark(
            task_id,
            task_status
        )

        print(f"Task marked successfully (ID: {task_id}) as {task_status!r}")

    
    @argument_count(0)
    def help(self) -> None:
        print("Supported actions")

        for action in self.operator:
            print(action)

        print("Read 'README.md' to see how to use the commands.")

    

def main() -> None:
    args = extract_rest(*sys.argv)

    if not args:
        print(
            "No command provided. "
            "Use 'help' to see available commands."
        )
        return

    cli = CLI(*args)
    cli.execute_operation()



if __name__ == "__main__":
    main()


