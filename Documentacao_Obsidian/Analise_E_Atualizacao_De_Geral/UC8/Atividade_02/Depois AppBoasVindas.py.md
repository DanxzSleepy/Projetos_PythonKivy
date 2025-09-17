```python
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class WelcomeApp(App):
    """Aplicativo de boas-vindas que recebe um nome e exibe mensagem personalizada."""
    
    def build(self):
        """Constrói a interface gráfica do aplicativo."""
        self._setup_layout()
        self._create_title_label()
        self._create_name_input()
        self._create_submit_button()
        self._create_message_label()
        
        return self.layout
    
    def _setup_layout(self):
        """Configura o layout principal do aplicativo."""
        self.layout = BoxLayout(orientation="vertical", padding=20, spacing=10)
    
    def _create_title_label(self):
        """Cria e adiciona o título do aplicativo."""
        self.title_label = Label(
            text="App de Boas-Vindas",
            font_size=28,
            bold=True,
            size_hint=(1, 0.2)
        )
        self.layout.add_widget(self.title_label)
    
    def _create_name_input(self):
        """Cria e adiciona o campo de entrada de nome."""
        self.name_input = TextInput(
            hint_text="Digite seu nome",
            multiline=False,
            size_hint=(1, 0.2)
        )
        self.layout.add_widget(self.name_input)
    
    def _create_submit_button(self):
        """Cria e adiciona o botão de envio."""
        self.submit_button = Button(
            text="Enviar",
            size_hint=(1, 0.2),
            background_color=(0.2, 0.6, 1, 1),
            font_size=20
        )
        self.submit_button.bind(on_press=self._handle_submission)
        self.layout.add_widget(self.submit_button)
    
    def _create_message_label(self):
        """Cria e adiciona o rótulo para exibir mensagens."""
        self.message_label = Label(
            text="",
            font_size=20,
            halign="center",
            valign="middle",
            size_hint=(1, 0.4)
        )
        self.layout.add_widget(self.message_label)
    
    def _handle_submission(self, instance):
        """Processa o envio do formulário e exibe mensagem de boas-vindas."""
        name = self.name_input.text.strip()
        
        if name:
            self.message_label.text = f"Bem-vindo(a), {name}!"
        else:
            self.message_label.text = "Por favor, digite seu nome."


if __name__ == "__main__":
    WelcomeApp().run()
```