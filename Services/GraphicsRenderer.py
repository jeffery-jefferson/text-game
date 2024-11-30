class GraphicsRenderer:
    def __init__(self):
        pass
    
    #region Public methods
    def DrawBanner(self, text, width, pady=0):
        if (width < len(text)):
            width = len(text)
        padx = int((width - 2 - len(text)) / 2)
        self.__drawline(width)
        for row in range(pady):
            self.__drawEmptyRowWithSideBorder(width)
        self.__drawTextWithPaddingAndSideBorder(text, padx, padx)
        for row in range(pady):
            self.__drawEmptyRowWithSideBorder(width)
        self.__drawline(width)
        
    def DrawTable(self, header="", *entries):
        # first look for longest entry
        longestEntry = len(header)
        for entry in entries:
            if not isinstance(entry, str):
                raise TypeError("Error when drawing table. Entries must be of type string.")
            if len(entry) > longestEntry:
                longestEntry = len(entry)
        # now calculate width
        width = longestEntry + 2
        # now draw header
        
        
    #endregion
    
    #region Private methods
    def __drawline(self, length=0):
        print("-" * length)
    def __drawEmptyRowWithSideBorder(self, length=0):
        print("|" + " " * (length - 2) + "|")
    def __drawTextWithPaddingAndSideBorder(self, text="", padL=0, padR=0):
        print("|" + " " * padL + text + " " * padR + "|")
    #endregion
    