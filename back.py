import os, sys
import rich
from rich.console import Console

console = Console()

back = console.input("[white]Back to main menu? [red]Y or N [white]> ")
if back == "Y":
   os.system("python3 main.py")

elif back == "N":
     sys.exit()
else:
    console.print("[bold red]Press Y or N")
