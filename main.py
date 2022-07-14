import os, sys
import rich
from rich.console import Console
from needed import set_packets
from needed import main_menu

console = Console()

def particle_main():
    try:
        set_packets={}
        main_menu={}
        menu = console.input("[red]choose option [white]> ")
        if menu == "1":
           console.print("[white]set tool: please wall...")
           os.system("git clone https://www.github.com/threat9/routersploit")
           os.system("python3 back.py")

        elif menu == "2":
             console.print("[white]set tool: please wall...")
             os.system("git clone https://github.com/rapid7/metasploit-framework")
             os.system("python3 back.py")

        elif menu == "3":
             console.print("[white]set tool: please wall...")
             os.system("git clone https://github.com/websploit/websploit")
             os.system("python3 back.py")

        elif menu == "4":
             console.print("[white]set tool: please wall...")
             os.system("git clone https://github.com/SLdevilX/Dbomber")
             os.system("python3 back.py")

        elif menu == "5":
             console.print("[white]set tool: please wall...")
             os.system("git clone https://github.com/LimerBoy/Impulse")
             os.system("python3 back.py")

        elif menu == "6":
             console.print("[white]set tool: please wall...")
             os.system("git clone https://github.com/Nikait/ni_bomber")
             os.system("python3 back.py")

        elif menu == "7":
             console.print("[white]set tool: please wall...")
             os.system("apt install wget -y")
             os.system("python3 back.py")

        elif menu == "8":
             console.print("[white]set tool: please wall...")
             os.system("pkg install python2 -y")
             os.system("python3 back.py")

        elif menu == "9":
             console.print("[white]set tool: please wall...")
             os.system("pkg install git -y")
             os.system("python3 back.py")

        elif menu == "Exit":
             console.print("\nBye!")
             sys.exit()

        elif menu == "Update":
             print("Developing.")

        elif menu == "dev":
            console.print('https://vk.com/rzcos')

    except KeyboardInterrupt:
        console.print('\n[bold red]Bye!')
        sys.exit()

particle_main()
