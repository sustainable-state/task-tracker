from datetime import datetime
import json


class JsonService:

    def add(self, task: str, status: str = "todo") -> None:
        date = datetime.now().strftime("%d-%m-%YT%H:%M")
        #id = self.get_id()
        return [self.generate_task(id=1, task=task, status=status, cr_date=date)]


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
    

    def get_id(self, json_name: str):
        try:
            with open(json_name, mode="r", encoding="utf-8") as file:
                json.load(file)
        
        except FileNotFoundError:
            raise 


