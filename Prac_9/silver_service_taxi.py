from taxi import Taxi

class SilverServiceTaxi(Taxi):
    """Represent a SilverServiceTaxi object."""

    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialize a SilverServiceTaxi instance.

        name: string, reference name for the taxi
        fuel: float, one unit of fuel drives one kilometre
        fanciness: float, scales the price_per_km
        """
        super().__init__(name, fuel, price_per_km=2)  # Assuming a base price_per_km value of 2
        self.price_per_km *= fanciness

    def get_fare(self):
        """Return the price for the taxi trip including flagfall."""
        base_fare = super().get_fare()  # Get the base fare (distance * adjusted price_per_km)
        return base_fare + self.flagfall  # Add the flagfall charge

    def __str__(self):
        """Return a string representation of the SilverServiceTaxi."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"
