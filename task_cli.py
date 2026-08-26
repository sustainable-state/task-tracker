import sys
from json_service import JsonService
from file_manager import extraction, FileManager

class CLI:
    def __init__(
            self, 
            cmd: str,
            *args: str,
            js_name: str = "tasks.json", 
        ) -> None:
        
        self.command = cmd
        self.args = args
        self.json_name = js_name
        self.js_service = JsonService()
        self.file_manager = FileManager()

    
    def application_run(self) -> None:
        json_add = getattr(self.js_service, self.command)
        file_add = getattr(self.file_manager, self.command)
        result = json_add(*self.args)
        file_add(self.json_name, result)



if __name__ == "__main__":
    cli = CLI(*extraction(*sys.argv))
    cli.application_run()