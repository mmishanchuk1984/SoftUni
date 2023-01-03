from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):
    AIR_CONDITIONER_FUEL_PER_KM = 0.9

    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__(fuel_quantity, fuel_consumption)

    def drive(self, distance):
        need_fuel = distance * (self.fuel_consumption + Car.AIR_CONDITIONER_FUEL_PER_KM)
        if need_fuel <= self.fuel_quantity:
            self.fuel_quantity -= need_fuel
        return self.fuel_quantity

    def refuel(self, fuel):
        self.fuel_quantity += fuel
        return self.fuel_quantity


class Truck(Vehicle):
    AIR_CONDITIONER_FUEL_PER_KM = 1.6

    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__(fuel_quantity, fuel_consumption)

    def drive(self, distance):
        need_fuel = distance * (self.fuel_consumption + Truck.AIR_CONDITIONER_FUEL_PER_KM)
        if need_fuel <= self.fuel_quantity:
            self.fuel_quantity -= need_fuel
            return self.fuel_quantity

    def refuel(self, fuel):
        self.fuel_quantity += (fuel * 0.95)
        return self.fuel_quantity * 0.95


car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)
