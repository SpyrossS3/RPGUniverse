# See Dev Notebook for comments and information.

class Menu:
    def __init__(me):
        me.option = input("Hi! Enter a menu option here: ")
        print(me.option)
    
    def mainMenu(me):
        if me.option == "1":
            print("TRUE")

class Game: 
    def __init__(me):
        menu = Menu()
        menu.mainMenu()

Game()