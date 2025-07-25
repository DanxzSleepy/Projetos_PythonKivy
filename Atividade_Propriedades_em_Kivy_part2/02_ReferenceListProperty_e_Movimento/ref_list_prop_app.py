# Objetivo: Agrupar pos_x e pos_y e movimentar um ponto.

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty

class MovableDot(Widget):
    pos_x = NumericProperty(100)
    pos_y = NumericProperty(100)
    dot_pos = ReferenceListProperty(pos_x, pos_y)

    def move_left(self):
        self.pos_x -= 10

    def move_right(self):
        self.pos_x += 10

    def move_up(self):
        self.pos_y += 10

    def move_down(self):
        self.pos_y -= 10

class RefListPropApp(App):
    def build(self):
        return MovableDot()

if __name__ == '__main__':
    RefListPropApp().run()
