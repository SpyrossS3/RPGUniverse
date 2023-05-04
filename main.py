# See Dev Notebook for comments and information.
from rich.console import Console
from rich.text import Text

console = Console()

class mainMenu:
    def __init__(me):
        me.option = input("Hi! Enter a menu option here: ")
        me.input = Text(me.option)
        me.input.stylize("bold cyan")
        console.print(me.input)
    
    def menu(me):
        if me.option == "1":
            console.print("TRUE", style="bold yellow")

class Game: 
    def __init__(me):
        mainmenu = mainMenu()
        mainmenu.menu()

Game()