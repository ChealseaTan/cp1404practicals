"""
The class
Estimated Time: 18 mins
Actual Time: 25 mins
"""

CURRENT_YEAR = 2023
VINTAGE_AGE = 50
class Guitar:

    def __init__(self, name="", year=0, cost=0):
        """Initialize a guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Convert object into string and print."""
        return f"{self.name} ({self.year}) : ${self.cost}"

    def get_age(self):
        """Calculate for guitar age."""
        age = CURRENT_YEAR - self.year
        return age

    def is_vintage(self):
        """Determine if the guitar is vintage."""
        return self.get_age() >= VINTAGE_AGE


