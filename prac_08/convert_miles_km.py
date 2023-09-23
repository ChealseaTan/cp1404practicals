from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934


class MilesConverterApp(App):
    """MilesConverterApp is a Kivy App for converting miles to kilometers."""
    output_text = StringProperty()

    def build(self):
        """Build the Kivy app from the kv file."""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        self.output_text = "54.71756"
        return self.root

    def get_validated_miles(self):
        """Validate the miles input."""
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0

    def handle_calculate(self):
        """Calculate for the kilometers."""
        miles = self.get_validated_miles()
        result = miles * MILES_TO_KM
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, change):
        """Increase/Decrease the miles and change the output."""
        miles = self.get_validated_miles()
        value = miles + change
        self.root.ids.input_miles.text = str(value)
        self.handle_calculate()


MilesConverterApp().run()
