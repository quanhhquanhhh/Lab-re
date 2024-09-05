class Mammal:
    __kingdom = "animals"

    def __init__(self, name, type, sound):
        self.__name = name
        self.__type = type
        self.__sound = sound

    def make_sound(self):
        if self.__sound:
            return f"{self.__name} makes {self.__sound}"
        else:
            return "No sound"

    def get_kingdom(self):
        if Mammal.__kingdom:
            return Mammal.__kingdom
        else:
            return "No kingdom set"

    def info(self):
        if self.__type:
            return f"{self.__name} is of type {self.__type}"
        else:
            return "Type is not set"


mammal = Mammal("Dog", "Domestic", "Bark")
print(mammal.make_sound())   
print(mammal.get_kingdom())  
print(mammal.info())         