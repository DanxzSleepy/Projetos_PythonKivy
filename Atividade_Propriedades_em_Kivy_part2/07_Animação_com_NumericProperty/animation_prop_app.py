from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty
from kivy.animation import Animation

class AnimatedBox(BoxLayout):
    box_size = NumericProperty(100)

    def animate_box(self):
        new_size = 200 if self.box_size == 100 else 100
        Animation(box_size=new_size, duration=0.5).start(self)

class AnimationApp(App):
    def build(self):
        return AnimatedBox()

if __name__ == '__main__':
    AnimationApp().run()

