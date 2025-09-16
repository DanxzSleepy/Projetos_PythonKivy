```python
from kivy.app import App
from kivy.uix.label import Label

class HelloWorldApp(App):

    def build(self):

        # Retorna um Label centralizado na tela

        return Label(

            text="Hello, World!",

            font_size=40,       # tamanho da fonte

            halign="center",    # alinhamento horizontal

            valign="middle"     # alinhamento vertical

        )

if __name__ == "__main__":

    HelloWorldApp().run()
```
