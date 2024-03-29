from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

UNIT_MILES_TO_KM = 1.60934


class MilesConverterApp(App):
    """MilesConverterApp is a Kivy App for converting miles into kilometres"""
    output_km = StringProperty()

    def build(self):
        """Build the Kivy app from the kv file."""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self):
        """Handle calculation (could be button press or other call)."""
        miles = self.convert_to_float()
        result = miles * UNIT_MILES_TO_KM
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, change):
        """Handle up and down button press, add the increment to the text input, call calculation function."""
        miles = self.convert_to_float() + change
        self.handle_calculate()
        self.root.ids.input_miles.text = str(miles)

    def convert_to_float(self):
        """Convert text into float if invalid."""
        try:
            miles = float(self.root.ids.input_miles.text)
            return miles
        except ValueError:
            return 0.0


MilesConverterApp().run()
