# Objetivo: Mudar dinamicamente o tema de cores da interface.

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import DictProperty

class ThemeRoot(BoxLayout):
    def toggle_theme(self):
        if App.get_running_app().app_theme['primary'] == [0.2, 0.6, 0.8, 1]:
            App.get_running_app().app_theme = {
                'primary': [0.8, 0.3, 0.2, 1],
                'secondary': [0.2, 0.2, 0.2, 1]
            }
        else:
            App.get_running_app().app_theme = {
                'primary': [0.2, 0.6, 0.8, 1],
                'secondary': [0.9, 0.9, 0.9, 1]
            }

class ThemedApp(App):
    app_theme = DictProperty({
        'primary': [0.2, 0.6, 0.8, 1],
        'secondary': [0.9, 0.9, 0.9, 1]
    })

    def build(self):
        return ThemeRoot()

if __name__ == '__main__':
    ThemedApp().run()


