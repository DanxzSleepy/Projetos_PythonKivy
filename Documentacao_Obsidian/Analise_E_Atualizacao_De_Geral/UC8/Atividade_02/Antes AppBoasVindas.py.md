```python
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput 


class WelcomeApp(App):
    def build(self):
        # Layout principal na vertical
        self.layout = BoxLayout(orientation="vertical", padding=20, spacing=10)
        # Título fixo no topo
        self.title_label = Label(
            text="App de Boas-Vindas",
            font_size=28,
            bold=True,
            size_hint=(1, 0.2)
        )
        self.layout.add_widget(self.title_label)
  
        # Campo de entrada
        self.name_input = TextInput(
            hint_text="Digite seu nome",
            multiline=False,
            size_hint=(1, 0.2)
        )

        self.layout.add_widget(self.name_input)

        # Botão estilizado
        self.button = Button(
            text="Enviar",
            size_hint=(1, 0.2),
            background_color=(0.2, 0.6, 1, 1),  # Azul
            font_size=20
        )
        self.button.bind(on_press=self.enviar)  # Evento do botão
        self.layout.add_widget(self.button)

        # Label da mensagem
        self.message_label = Label(
            text="",
            font_size=20,
            halign="center",
            valign="middle",
            size_hint=(1, 0.4)
        )
        self.layout.add_widget(self.message_label)

        return self.layout
  
    def enviar(self, instance):
        nome = self.name_input.text.strip()
        if nome:
            self.message_label.text = f"Bem-vindo(a), {nome}!"
        else:
            self.message_label.text = "Por favor, digite seu nome."  


# Rodar o app
if __name__ == "__main__":
    WelcomeApp().run()
```