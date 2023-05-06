# See Dev Notebook for comments and information.
from rich.console import Console
from rich.text import Text
from rich.theme import Theme

game_theme = Theme({
    "title": "#16c60c",
    "info": "#3a96dd",
    "options": "#f9f1a5"
})
#Need to define the size of the app window
console = Console(theme=game_theme)

class mainMenu:
    def __init__(me):
        me.title = Text("RPGUniverse", "title", justify="center")
        me.title.align("center", 100,)
        console.print(me.title)
        console.print("\n \n \n")
        optext = Text("<1.Start>", style="options")
        optext.align("center", 100)
        console.print(optext)
        optext = Text("<2.How to play>", style="options")
        optext.align("center", 100)
        console.print(optext)
        optext = Text("<3.Exit>", style="options")
        optext.align("center", 100)
        console.print(optext)

        me.option = input(">>> ")
        me.input = Text(me.option, "options")
        console.print(me.input)
    
    def menu(me):
        if me.option == "1":
            console.print("TRUE", style="yellow")
            pass
        if me.option == "2":
            console.print("TRUE", style="yellow")
            pass
        if me.option == "3":
            console.print("Thank you for playing, goodbye. :)")
            pass
        #If this is else instead of elif, it still gives the error msg after running the other code
        elif me.option != "1" and me.option != "2" and me.option != "3":
            #Make this red as it is an error, and make orange/brown a warning color
            console.print("INVALID INPUT!!!")

class Game: 
    def __init__(me):
        mainmenu = mainMenu()
        mainmenu.menu()

Game()