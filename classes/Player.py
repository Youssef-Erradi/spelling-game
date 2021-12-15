class Player:
    
    def __init__(self, name="", level=0):
        self.set_name(name)
        self.set_score(0)
        self.set_level(level)

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def get_level(self):
        return self.__level

    def set_name(self, value):
        if(value == None) : raise ValueError("Player name cannot be None")
        value = value.strip()
        if(value == "") : raise ValueError("Player name cannot be an empty string")
        self.__name = value

    def set_score(self, value):
        if(value == None or value < 0) : raise ValueError("Player score cannot be None nor negative")
        self.__score = value

    def set_level(self, value):
        if(value == None or value < 0) : raise ValueError("Player level cannot be None nor negative")
        self.__level = value
    
    def increment_score(self):
        self.__score += ((self.__level+1)*10)
    
    def __str__(self):
        return f"Player name = {self.__name}, Level = {self.__level}, score = {self.__score}"
    
    def __iter__(self):
        iters = dict((x,y) for x,y in self.__dict__.items() if x[:2] != '__')
        iters.update(self.__dict__)
        for x,y in iters.items():
            yield x.replace("_Player__",""),y
