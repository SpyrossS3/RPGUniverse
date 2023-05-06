# See Dev Notebook for comments and information.
from rich.console import Console
from rich.text import Text

console = Console()

class mainMenu:
    def __init__(me):
        me.title = Text("RPGUniverse")
        me.title.stylize("bold underline yellow")
        me.title.align("center", 115)
        console.print(me.title)
        me.option = input("Hi! Enter a menu option here: ")
        me.input = Text(me.option)
        me.input.stylize("cyan")
        console.print(me.input)
    
    def menu(me):
        if me.option == "1":
            console.print("TRUE", style="bold yellow")

class Game: 
    def __init__(me):
        mainmenu = mainMenu()
        mainmenu.menu()

Game()