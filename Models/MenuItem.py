class MenuItem:
    def __init__(self, label, description=None, action=None):
        self.label = label
        self.description = description
        self._action = action
    
    def __str__(self):
        if self.description == None or self.description == "":
            return self.label
        return f'{self.label} - {self.description}'
    
    def Evoke(self):
        self._action()