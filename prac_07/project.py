"""
The class
Estimated Time: 1 hour
Actual Time:
"""


class Project:

    def __init__(self, name="", start_date="", priority=0, cost_estimate=0, completion_percentage=0):
        """Initialize a guitar instance."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        """Convert object into string and print."""
        return f"{self.name}, start: {self.start_date}, priority {self.priority}, estimate: ${self.cost_estimate}, completion: {self.completion_percentage}%"


