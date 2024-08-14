class Band:
    """Band class to manage a list of musicians."""

    def __init__(self, name):
        """Initialize a Band with a name and an empty list of musicians."""
        self.name = name
        self.musicians = []

    def add(self, musician):
        """Add a musician to the band."""
        self.musicians.append(musician)

    def __str__(self):
        """Return a string representation of the band with all musicians and their instruments."""
        musician_details = ', '.join(str(musician) for musician in self.musicians)
        return f"{self.name} ({musician_details})"

    def play(self):
        """Simulate playing music by having each musician play their first instrument or state if they need one."""
        return '\n'.join(musician.play() for musician in self.musicians)
