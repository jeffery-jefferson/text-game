from Models.User import User
import json

class UserRepo:
    @staticmethod
    def GetUserByUserNameAndPassword(username, password) -> User:
        with open("Data/Users.txt", "r") as f:
            for line in f.readlines():
                obj = json.loads(line)
                if obj["_username"] == username and obj["_password"] == password:
                    return User(obj["_username"], obj["_password"], obj["_birthday"])
        return None
    
    @staticmethod
    def GetUserByUsername(username) -> User:
        with open("Data/Users.txt", "r") as f:    
            for line in f.readlines():
                obj = json.loads(line)
                if obj["_username"] == username:
                    return User(obj["_username"], obj["_password"], obj["_birthday"])
        return None

    @staticmethod
    def AddUser(user) -> None:
        if not isinstance(user, User):
            raise TypeError("user must be of typer User")
        with open("Data/Users.txt", "a") as f:
            f.write(user.ToJson())