import random
from prac_06.car import Car


class UnreliableCar(Car):
    """UnreliableCar version of a car."""

    def __init__(self, name, fuel, reliability):
        """Initialise a UnreliableCar instance."""
        super().__init__(name, fuel)
        self.reliability = float(reliability)

    def drive(self, distance):
        """Drive the car based on reliability."""
        random_number = random.randint(0, 100)
        if random_number < self.reliability:
            distance_travelled = super().drive(distance)
        else:
            distance_travelled = 0
        return distance_travelled
