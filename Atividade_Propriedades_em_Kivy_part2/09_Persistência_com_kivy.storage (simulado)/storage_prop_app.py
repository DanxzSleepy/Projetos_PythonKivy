from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty
import json
import os

STORAGE_PATH = "counter_data.json"

class PersistentCounter(BoxLayout):
    count = NumericProperty(0)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.load_data()

    def increment(self):
        self.count += 1

    def load_data(self):
        if os.path.exists(STORAGE_PATH):
            with open(STORAGE_PATH, 'r') as f:
                data = json.load(f)
                self.count = data.get('count', 0)

    def save_data(self):
        with open(STORAGE_PATH, 'w') as f:
            json.dump({'count': self.count}, f)

class StoragePropApp(App):
    def build(self):
        self.counter = PersistentCounter()
        return self.counter

    def on_stop(self):
        self.counter.save_data()

if __name__ == '__main__':
    StoragePropApp().run()
