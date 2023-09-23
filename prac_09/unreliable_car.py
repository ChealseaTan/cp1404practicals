import random
from prac_09.car import Car


class UnreliableCar(Car):
    """Represent Unreliable Car."""
    def __init__(self, name, fuel, reliability: float):
        """Initialise an Unreliable Car instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Calculate distance driven."""
        if (random.randint(0, 100)) >= self.reliability:
            distance = 0
        distance_driven = super().drive(distance)
        return distance_driven
