from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import BooleanProperty, ObjectProperty
from kivy.lang import Builder

Builder.load_file("nested_prop.kv")

class StatusIndicator(BoxLayout):
    is_active = BooleanProperty(False)

class MainControlWidget(BoxLayout):
    status_obj = ObjectProperty(None)

    def alternar_status(self):
        self.status_obj.is_active = not self.status_obj.is_active

class NestedPropApp(App):
    def build(self):
        return MainControlWidget()

if __name__ == '__main__':
    NestedPropApp().run()
