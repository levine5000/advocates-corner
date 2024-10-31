class Fruits:
    #constructor method
    def __init__(self, name, price, color):
        self.name = name
        self.price = price
        self.color = color
    def display(self):
        #method
        print(f"I love eating {self.name},it cost {self.price} and it is {self.color} in color")

#instance
myobj=Fruits("Banana", 20, "Yellow")
myobj.display()