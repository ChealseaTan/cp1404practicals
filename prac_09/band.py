class Band:
    def __init__(self, mode=""):
        self.mode = mode
        self.members = []

    def __str__(self):
        return f"{self.mode} ({', '.join(str(member) for member in self.members)})"

    def __repr__(self):
        """Return a string representation of a Musician, showing the variables."""
        return str(vars(self))

    def add(self, member):
        return self.members.append(member)

    def play(self):
        for self.member in self.members:
            return f"{self.member}"
