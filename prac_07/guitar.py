THIS_YEAR = 2024
VINTAGE_AGE = 50


class Guitar:
    """Represent information about a Guitar language."""
    def __init__(self, name="", year=0, cost=0.0):
        """Construct a Guitar from the given values."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return string representation of a Guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:.2f}"

    def __lt__(self, other):
        """Compare the guitars by year."""
        return self.year < other.year

    def get_age(self):
        """Calculate the age of a guitar."""
        return THIS_YEAR - self.year

    def is_vintage(self):
        """Determine whether the age of a guitar is more than the vintage age."""
        return self.get_age() >= VINTAGE_AGE


