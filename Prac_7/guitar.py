
class Guitar:
    """Represent a guitar"""

    def __init__(self, name, year, cost):
        """Initialise a Guitar instance"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of a Guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:.2f}"

    def __lt__(self, other):
        """Define the less-than operator for sorting by year"""
        return self.year < other.year

