
import random
from car import Car  # Importing the Car class from car.py

class UnreliableCar(Car):
    """Represent an UnreliableCar object."""

    def __init__(self, name, fuel, reliability):
        """Initialize an UnreliableCar instance.

        name: string, reference name for the car
        fuel: float, one unit of fuel drives one kilometre
        reliability: float, percentage chance that the car will drive
        """
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car a given distance with reliability check.

        Drive the car only if a random number is less than reliability.
        """
        if random.randint(0, 100) < self.reliability:
            return super().drive(distance)
        else:
            return 0  # Car didn't drive due to reliability failure
