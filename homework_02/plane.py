"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload


class Plane(Vehicle):
    def __init__(self, weight, fuel, fuel_consumption, max_cargo, cargo=0):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.max_cargo = max_cargo
        self.cargo = cargo

    def load_cargo(self, amount):
        if self.cargo + amount > self.max_cargo:
            raise CargoOverload("overload")
        else:
            self.cargo += amount

    def remove_all_cargo(self):
        cargo = self.cargo
        self.cargo = 0
        return cargo
