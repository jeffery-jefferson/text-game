from Services.App import App
from Services.LoginService import LoginService

if __name__ == "__main__":
    print("Loading environment...");
    user = LoginService.Login()
    
    if user is None:
        print("Have a nice day!")
        exit()
        
    app = App(user)
    app.Run()