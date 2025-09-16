```Python
import random
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Line, Rectangle, Ellipse
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.slider import Slider
from kivy.uix.spinner import Spinner


class PaintingCanvas(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.line_width = 2
        self.current_shape = 'Line'
        self.shape_start_positions = {}  # Armazena posições iniciais para formas

    def on_touch_down(self, touch):
        red, green, blue = [random.random() for _ in range(3)]
        
        with self.canvas:
            Color(red, green, blue)
            
            if self.current_shape == 'Line':
                touch.ud['line'] = Line(points=(touch.x, touch.y), width=self.line_width)
            elif self.current_shape == 'Rectangle':
                self.shape_start_positions[touch] = (touch.x, touch.y)
                touch.ud['rect'] = Rectangle(pos=(touch.x, touch.y), size=(1, 1))
            elif self.current_shape == 'Ellipse':
                self.shape_start_positions[touch] = (touch.x, touch.y)
                touch.ud['ellipse'] = Ellipse(pos=(touch.x, touch.y), size=(1, 1))

    def on_touch_move(self, touch):
        if self.current_shape == 'Line' and 'line' in touch.ud:
            touch.ud['line'].points += [touch.x, touch.y]
        elif self.current_shape in ['Rectangle', 'Ellipse'] and touch in self.shape_start_positions:
            start_x, start_y = self.shape_start_positions[touch]
            width = touch.x - start_x
            height = touch.y - start_y
            size = (abs(width), abs(height))
            position = (min(start_x, touch.x), min(start_y, touch.y))
            
            if self.current_shape == 'Rectangle':
                touch.ud['rect'].pos = position
                touch.ud['rect'].size = size
            elif self.current_shape == 'Ellipse':
                touch.ud['ellipse'].pos = position
                touch.ud['ellipse'].size = size

    def clear_canvas(self):
        self.canvas.clear()

    def set_line_width(self, width):
        self.line_width = width

    def set_shape(self, shape_name):
        self.current_shape = shape_name


class PaintingApp(App):
    def build(self):
        layout = FloatLayout()
        canvas = PaintingCanvas()
        layout.add_widget(canvas)

        # Botão Limpar
        clear_button = Button(
            text='Limpar', 
            size_hint=(0.15, 0.1), 
            pos_hint={'x': 0.82, 'y': 0.88}
        )
        clear_button.bind(on_release=lambda instance: canvas.clear_canvas())
        layout.add_widget(clear_button)

        # Controle de espessura da linha
        width_slider = Slider(
            min=1, 
            max=10, 
            value=2, 
            size_hint=(0.5, 0.05), 
            pos_hint={'x': 0.02, 'y': 0.9}
        )
        width_slider.bind(value=lambda instance, value: canvas.set_line_width(value))
        layout.add_widget(width_slider)

        # Seletor de forma
        shape_selector = Spinner(
            text='Line',
            values=('Line', 'Rectangle', 'Ellipse'),
            size_hint=(0.2, 0.07),
            pos_hint={'x': 0.55, 'y': 0.88}
        )
        shape_selector.bind(text=lambda instance, text: canvas.set_shape(text))
        layout.add_widget(shape_selector)

        return layout


if __name__ == '__main__':
    PaintingApp().run()
```