from Data.UserRepo import UserRepo
from Models.User import User
from getpass import getpass
from datetime import datetime
from Constants import Constants

class LoginService:
    @staticmethod
    def Login() -> User:
        username = input("Username: ")
        password = getpass()
        
        # Get user from the repository
        user = UserRepo.GetUserByUsername(username)
        
        if user is not None:
            if user._password != password:
                print("Incorrect password.")
                return None
        else: # If user does not exist, prompt for birthday
            retryCount = 3
            while True:
                try:
                    # if they fail to enter a valid birthday they don't deserve the rest of the program
                    if retryCount == 0:
                        print("You are stupid.")
                        return None
                    
                    birthday_input = input("Birthday (YYYY-MM-DD): ")
                    birthday = datetime.strptime(birthday_input, Constants.DATE_FORMAT)
                    break  # Exit loop if date is valid
                except ValueError:  # Catch specific exception for date format issues
                    print("Invalid Birthday. Please try again.")
                    print(f"Retries remaining: {retryCount}")
                    retryCount -= 1
            
            # Create new user and add to the repository
            user = User(username, password, birthday)
            UserRepo.AddUser(user)
        
        # Return the user (existing or newly created)
        print("\n\n\nLogin Successful.\n\n\n")
        return user
