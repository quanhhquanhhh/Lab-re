class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        if self.__name:
            return self.__name
        else:
            return "Name is not set"

    def get_age(self):
        if self.__age:
            return self.__age
        else:
            return "Age is not set"


person = Person("George", 32)
print(person.get_name())  
print(person.get_age())  