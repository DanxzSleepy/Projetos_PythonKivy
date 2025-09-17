```python
from kivy.app import App
from kivy.uix.label import Label


class HelloWorldApp(App):
    """Aplicativo simples que exibe 'Hello, World!' centralizado na tela."""
    
    def build(self):
        """Constrói e retorna a interface gráfica do aplicativo."""
        return Label(
            text="Hello, World!",
            font_size=40,
            halign="center",
            valign="middle"
        )


if __name__ == "__main__":
    HelloWorldApp().run()
```