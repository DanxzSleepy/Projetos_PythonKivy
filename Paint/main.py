from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse, Line


class MeuPaintWidget(Widget):
    def on_touch_down(self, touch):
        with self.canvas:
            color = (1, 1, 0)
            d = 30.
            Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))


class MeuPaintApp(App):
    def build(self):
        return MeuPaintWidget()

if __name__ == '__main__':
    MeuPaintApp().run()