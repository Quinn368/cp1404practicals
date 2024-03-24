class Project:
    """Represent information about a Project language."""
    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """Construct a Project from the given values."""
        self.name = name
        self.start_date = start_date
        self.priority = int(priority)
        self.cost_estimate = float(cost_estimate)
        self.completion_percentage = int(completion_percentage)

    def __repr__(self):
        """Return string representation of a Guitar."""
        return f"{self.name}, start: {self.start_date}, priority {self.priority}, estimate: ${self.cost_estimate:.2f}, completion: {self.completion_percentage}%"

    def line_format(self):
        """Return in string in a formatted form."""
        return f"{self.name}\t{self.start_date}\t{self.priority}\t{self.cost_estimate:.2f}\t{self.completion_percentage}"

    def is_completed(self):
        """Check is completion of percentage is completed."""
        return self.completion_percentage == 100
