from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """Kivy app to demo dynamic label creation."""
    def __init__(self):
        """Initiate a list of names."""
        super().__init__()
        self.names = ["Bobby Brown", "Gerald Green", "Whitney White"]

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        """Create labels for every name in names."""
        for name in self.names:
            temporary_label = Label(text=name)
            self.root.ids.main.add_widget(temporary_label)


DynamicLabelsApp().run()

