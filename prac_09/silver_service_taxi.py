from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised version of a Taxi that includes fanciness."""
    flag_value = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialise a Silver Service Taxi instance, based on parent class Taxi."""
        super().__init__(name, fuel)
        self.price_per_km *= fanciness

    def __str__(self):
        """Return string with Taxi information and total price."""
        return f"{super().__str__()} plus flagfall of ${self.flag_value}, total fare price = ${self.get_fare()}"

    def get_fare(self):
        """Return the price for the taxi trip."""
        incomplete_fare = super().get_fare()
        return incomplete_fare + self.flag_value

