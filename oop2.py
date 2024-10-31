class Person:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age
    def display(self):
        print(f"The boy's name is {self.name}, a 5'2 {self.gender}, around {self.age}, plays basketball")

myobj = Person("Jake", "Male", 23)
myobj.display()