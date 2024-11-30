from .MenuItem import MenuItem

class ConsoleMenu:
    def __init__(self):
        self._items = []
        
    def PushMenuItem(self, item):
        if not isinstance(item, MenuItem):
            raise TypeError("Item must be of type MenuItem.")
        self._items.append(item)
    
    def PopMenuItem(self, item):
        if not isinstance(item, MenuItem):
            raise TypeError("Item must be of type MenuItem")
        self._items.pop()
        
    def Display(self, isNumbered=False):
        for i in range(0, len(self._items)):
            if isNumbered:
                print(f'{i}. {self._items[i]}')
            else:
                print(self._items[i])

    # Evokes the method associated with the i'th item of the menu
    def Evoke(self, i):
        try:
            if isinstance(i, str):
                i = int(i)
            item = self._items[i]
            item.Evoke()
        except ValueError:
            print(f"Invalid option: please enter a number.")
        except IndexError:
            print(f"Invalid option: '{i}' out of range.")
        except:
            print(f"Error when executing option '{i}', command: {item.label}.")    
    