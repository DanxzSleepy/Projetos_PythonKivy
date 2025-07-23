from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.graphics import Ellipse, Color
from kivy.properties import NumericProperty, ReferenceListProperty
from kivy.lang import Builder

Builder.load_file("ref_list_prop.kv")

class MovableDot(Widget):
    pos_x = NumericProperty(100)
    pos_y = NumericProperty(100)
    dot_pos = ReferenceListProperty(pos_x, pos_y)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Color(1, 0, 0)
            self.dot = Ellipse(pos=self.dot_pos, size=(30, 30))
        self.bind(dot_pos=self.update_dot)

    def update_dot(self, *args):
        self.dot.pos = self.dot_pos

    def move_left(self):  self.pos_x -= 10
    def move_right(self): self.pos_x += 10
    def move_up(self):    self.pos_y += 10
    def move_down(self):  self.pos_y -= 10

class MainWidget(BoxLayout):  # container com ID
    pass

class RefListPropApp(App):
    def build(self):
        return MainWidget()

if __name__ == '__main__':
    RefListPropApp().run()
