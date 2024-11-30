from .GraphicsRenderer import GraphicsRenderer
from Models.ConsoleMenu import ConsoleMenu 
from Models.MenuItem import MenuItem
from Models.User import User

class App:
    def __init__(self, user):
        self.renderer = GraphicsRenderer()
        self.user = user
        
        # creating the help menu
        i1 = MenuItem("Help", "", self.__help)
        i2 = MenuItem("Play")
        i3 = MenuItem("Tarot")
        self.mainMenu = ConsoleMenu()
        self.mainMenu.PushMenuItem(i1)
        self.mainMenu.PushMenuItem(i2)
        self.mainMenu.PushMenuItem(i3)
        
        # creating the console menu
        h1 = MenuItem("x, X, exit, stop", "Exits the program")
        h2 = MenuItem("Help", "shows the help menu")
        h3 = MenuItem("Play", "Plays a text adventure game")
        h4 = MenuItem("Tarot", "Performs a tarot reading")
        self.helpMenu = ConsoleMenu()
        self.helpMenu.PushMenuItem(h1)
        self.helpMenu.PushMenuItem(h2)
        self.helpMenu.PushMenuItem(h3)
        self.helpMenu.PushMenuItem(h4)
        
    #region Public Methods
    def Run(self) -> None:
        self.renderer.DrawBanner(f"Welcome '{self.user._username}' to Text-v1", 40, 1)
        print("Please choose an option:")
        self.mainMenu.Display(True)
        print()
        
        while True:
            # run the program
            choice = input("> ")
            
            # exit program
            if choice == 'x' or choice == 'X' or choice == 'exit' or choice == 'stop':
                break
            
            self.mainMenu.Evoke(choice)
            
    #endregion
    
    #region Private Methods
    def __help(self) -> None:
        self.helpMenu.Display()
    #endregion