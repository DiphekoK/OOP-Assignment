# 🎭 Base class: Vehicle
class Vehicle:
    def move(self):
        return "Moving..."

# 🎭 Subclasses with unique move() implementations
class Car(Vehicle):
    def move(self):
        return "Driving 🚗"

class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"

class Boat(Vehicle):
    def move(self):
        return "Sailing 🚢"

# Creating objects
car = Car()
plane = Plane()
boat = Boat()

# Demonstrating polymorphism
print(car.move())   # Output: Driving 🚗
print(plane.move()) # Output: Flying ✈️
print(boat.move())  # Output: Sailing 🚢
