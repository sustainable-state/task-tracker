from datetime import datetime
from utils import current_datetime, generate_id, get_tasks_id
from json_manager import JsonManager


class TaskService:
    def __init__(self, js_name: str):
        self.js_name = js_name
        self.js_manager = JsonManager(js_name)
        

    def add(self, task: str, status: str = "todo") -> None:
        tasks = self.js_manager.read()
        date = current_datetime()
        id = generate_id(tasks=tasks)

        if tasks is None:
            tasks = []
        
        tasks.append(self.generate_task(id=id, task=task, status=status, cr_date=date))
        self.js_manager.add(tasks=tasks)

    
    def update(self, id: int, description: str) -> None:
        print("UPDATE:")
        print("id:", id, type(id))
        print("description:", description, type(description))

        tasks = self.js_manager.read()

        print("READ:", tasks)

        if tasks is None:
            print("TASKS IS NONE")
            return

        if id in get_tasks_id(tasks):
            print("ID FOUND")

            for task in tasks:
                print("CHECK:", task["id"], type(task["id"]))

                if task["id"] == id:
                    print("TASK FOUND:", task)

                    task["description"] = description
                    task["updatedAt"] = current_datetime()

                    print("CHANGED:", task)
                    break
        else:
            print("ID NOT FOUND")

        print("BEFORE ADD:", tasks)

        self.js_manager.add(tasks=tasks)

        print("ADD FINISHED")


    def generate_task(
            self,
            id: int, 
            task: str, 
            status: str, 
            cr_date: datetime,
            up_date: datetime | None = None
        ) -> dict:

        return {
            "id": id,
            "description": task,
            "status": status,
            "createdAt": cr_date,
            "updatedAt": up_date
        }


