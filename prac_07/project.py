"""
The class
Estimated Time: 45mins
Actual Time:
"""
from datetime import datetime
COMPLETED_PERCENTAGE = 100


class Project:

    def __init__(self, name: str, start_date: datetime.date, priority=0, cost_estimate=0, completion_percentage=0):
        """Initialize a project instance."""
        self.name = name
        self.start_date = start_date
        self.priority = int(priority)
        self.cost_estimate = float(cost_estimate)
        self.completion_percentage = int(completion_percentage)

    def __str__(self):
        """Convert object into string and print."""
        return f"{self.name}, start: {self.start_date}, priority {self.priority}, estimate: ${self.cost_estimate}, completion: {self.completion_percentage}%"

    def is_completed(self):
        """Determine if the project is completed."""
        return int(self.completion_percentage) == COMPLETED_PERCENTAGE

    def __lt__(self, other):
        """Get the smallest to the biggest priority."""
        return self.priority < other.priority

