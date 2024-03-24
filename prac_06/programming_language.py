class ProgrammingLanguage:
    """Represent a ProgrammingLanguage object."""
    def __init__(self, field="", typing="", reflection=False, year=0):
        """Initialise a ProgrammingLanguage instance."""
        self.field = field
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        return f"{self.field}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        """Check whether typing is Dynamic"""
        return self.typing == "Dynamic"
