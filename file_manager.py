import os
import json

class FileManager:
    def json_existence(self, json_name: str) -> None:
        if json_name not in os.listdir():
            with open(json_name, "w", encoding="utf-8") as file:
                pass

    
    def add(self, json_name: str, task: dict) -> None:
        with open(json_name, "w", encoding="utf-8") as file:
            json.dump(task, file, indent=4)
        
        print("task succesfully added")
        



def extraction(*args):
    _, *other = args
    return other