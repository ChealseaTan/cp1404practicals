"""
The class
Estimated Time: 15 mins
Actual Time: 20 mins
"""


class ProgrammingLanguage:

    def __init__(self, name="", typing="", reflection=False, year=0):
        """Initialize a programming language instance."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Convert object into string and print."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        """Determine if the typing is dynamic."""
        return self.typing == "Dynamic"
