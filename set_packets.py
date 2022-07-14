import rich
import os, sys
from rich.console import Console

console = Console()

set = console.input("[white]set the required packages? [red]Y or N [white]> ")
if set == "Y":
   os.system("pip3 install -r requirements.txt")

