
class Band:
    def __init__(self, name=""):
        """Initiate a Band instance."""
        self.name = name
        self.members = []

    def __str__(self):
        """Return band string."""
        return f"{self.name} ({', '.join(str(member) for member in self.members)})"

    def add(self, member):
        """Add a member to the band."""
        return self.members.append(member)

    def play(self):
        """Display the band members playing their instrument."""
        result = ""
        for member in self.members:
            result += member.play() # + "\n"
            print("\n")
        return result
