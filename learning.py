# Class is a Template 
# Objects are instances of a Class

class Car:

    # Class Vars
    speed = 0

    # Constructor
    def __init__(self, brand : str, model : str):
        self.brand = brand
        self.model = model
        
    # Methods
    def accelerate(self, inc):
        self.speed += inc
        return self.speed

    def display_status(self):
        print(f"Your Car [Brand: {self.brand}, Model: {self.model}, Current Speed: {self.speed}]")

# Instantiate Object
my_car = Car("Mercedes", "ML350")

# Call Method
my_car.accelerate(20)
my_car.display_status()