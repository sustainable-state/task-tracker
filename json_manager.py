import json
from decorator import require_json_file

class JsonManager:
    def __init__(self, js_name: str) -> None:
        self.js_name = js_name
        

    def add(self, tasks: dict) -> None:
        with open(self.js_name, "w", encoding="utf-8") as file:
            json.dump(tasks, file, indent=4)
    

    @require_json_file
    def read(self) -> dict:
        try:
            with open(self.js_name, "r", encoding="utf-8") as file:
                return json.load(file)
        except json.decoder.JSONDecodeError:
            return []
