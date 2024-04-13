class Band:
    """Represent Band class."""
    def __init__(self, name):
        """Initialise a Band class."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of a Band."""
        musician_info = ', '.join(str(musician) for musician in self.musicians)
        return f"{self.name} ({musician_info})"

    def add(self, musician):
        """Add a musician to the band."""
        self.musicians.append(musician)

    def play(self):
        """Simulate the band playing by calling the play method of each musician."""
        for musician in self.musicians:
            print(musician.play())
