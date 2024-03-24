THIS_YEAR = 2024
VINTAGE_AGE = 50


class Guitar:
    """Represent a Guitar object."""
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Calculate how old the guitar is."""
        return THIS_YEAR - self.year

    def is_vintage(self):
        """Check is the guitar is more than 50 years old."""
        return self.get_age() >= VINTAGE_AGE
