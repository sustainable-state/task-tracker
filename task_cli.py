import os
import sys



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

        print(cmd, args)


        self.run()

    
    def run(self) -> None:
        self.json_existence()


    def json_existence(self):
        if self.json_name not in os.listdir():
            with open(self.json_name, "w", encoding="utf-8") as file:
                pass
        

def sys_extraction(*args):
    _, *other = args
    return other

if __name__ == "__main__":
    cli = CLI(*sys_extraction(*sys.argv))