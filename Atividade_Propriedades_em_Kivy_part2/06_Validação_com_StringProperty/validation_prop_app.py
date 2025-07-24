from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
import re

class ValidatedInputWidget(BoxLayout):
    _validated_text = "Texto válido"

    def get_text(self):
        return self._validated_text

    def set_text(self, value):
        if len(value) >= 5 and not re.search(r'\d', value):
            self._validated_text = value

    validated_text = StringProperty()
    validated_text = property(get_text, set_text)

class ValidationApp(App):
    def build(self):
        return ValidatedInputWidget()

if __name__ == '__main__':
    ValidationApp().run()
