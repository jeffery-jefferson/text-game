import json
from datetime import date
from Constants import Constants

class User:
    def __init__(self, username, password, birthday):
        self._username = username
        self._password = password
        if not isinstance(birthday, date) and not isinstance(birthday, str):
            raise TypeError("'birthday' must be of type 'date' or 'str'")
        self._birthday = date.strftime(birthday, Constants.DATE_FORMAT) if isinstance(birthday, date) else birthday
        
    def ToJson(self) -> str:
        return json.dumps(self, default=lambda obj: obj.__dict__)