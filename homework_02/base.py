from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    def __init__(self, weight=0, fuel=0, fuel_consumption=0):
        self.weight = weight
        self.started = False
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError
        else:
            print(f'The Vehicle started')

    def move(self, distance):
        fuel_needed = distance * self.fuel_consumption
        if self.fuel < fuel_needed or self.fuel < self.fuel_consumption:
            raise NotEnoughFuel
        else:
            self.fuel -= fuel_needed
