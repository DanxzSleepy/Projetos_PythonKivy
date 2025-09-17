```python
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.image import Image


class Colors:
    """Paleta de cores no estilo retrô neon."""
    BACKGROUND = (0, 0, 0, 1)          # Fundo preto estilo terminal
    TITLE_COLOR = (0, 1, 0.6, 1)       # Verde neon
    BUTTON_COLOR = (1, 0.2, 0.8, 1)    # Rosa neon
    ERROR_COLOR = (1, 0, 0, 1)         # Vermelho
    WARNING_COLOR = (1, 1, 0, 1)       # Amarelo forte
    INFO_COLOR = (0.3, 0.8, 1, 1)      # Azul neon
    SUCCESS_COLOR = (0, 1, 0, 1)       # Verde neon brilhante


class AgeVerificationForm(BoxLayout):
    """Formulário para verificação de faixa etária com tema retrô."""
    
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", padding=20, spacing=15, **kwargs)
        self._setup_ui_components()
    
    def _setup_ui_components(self):
        """Configura todos os componentes da interface do usuário."""
        self._create_title_label()
        self._create_name_input()
        self._create_age_input()
        self._create_verify_button()
        self._create_message_label()
        self._create_feedback_icon()
    
    def _create_title_label(self):
        """Cria o rótulo de título com estilo retrô."""
        self.title_label = Label(
            text="IDADE - Verificador de Faixa Etária",
            font_size=28,
            bold=True,
            color=Colors.TITLE_COLOR,
            size_hint=(1, 0.2)
        )
        self.add_widget(self.title_label)
    
    def _create_name_input(self):
        """Cria o campo de entrada para nome no estilo terminal."""
        self.name_input = TextInput(
            hint_text="Digite seu nome...",
            multiline=False,
            size_hint=(1, 0.15),
            background_color=(0, 0, 0, 1),
            foreground_color=Colors.SUCCESS_COLOR,
            cursor_color=Colors.BUTTON_COLOR,
            font_size=18
        )
        self.add_widget(self.name_input)
    
    def _create_age_input(self):
        """Cria o campo de entrada para idade com validação numérica."""
        self.age_input = TextInput(
            hint_text="Digite sua idade...",
            multiline=False,
            input_filter="int",
            size_hint=(1, 0.15),
            background_color=(0, 0, 0, 1),
            foreground_color=Colors.SUCCESS_COLOR,
            cursor_color=Colors.BUTTON_COLOR,
            font_size=18
        )
        self.age_input.bind(on_text_validate=self._validate_input)
        self.add_widget(self.age_input)
    
    def _create_verify_button(self):
        """Cria o botão de verificação com estilo neon."""
        self.verify_button = Button(
            text="VERIFICAR",
            size_hint=(1, 0.2),
            background_normal='',
            background_color=Colors.BUTTON_COLOR,
            font_size=20,
            color=(0, 0, 0, 1)  # Texto preto para contraste
        )
        self.verify_button.bind(on_press=self._verify_age)
        self.add_widget(self.verify_button)
    
    def _create_message_label(self):
        """Cria o rótulo para exibir mensagens com estilo CRT."""
        self.message_label = Label(
            text="",
            font_size=20,
            halign="center",
            valign="middle",
            size_hint=(1, 0.3),
            color=Colors.SUCCESS_COLOR,
            markup=True
        )
        self.message_label.bind(size=self._adjust_text_wrapping)
        self.add_widget(self.message_label)
    
    def _create_feedback_icon(self):
        """Cria o ícone de feedback visual."""
        self.feedback_icon = Image(size_hint=(None, None), size=(50, 50))
        self.add_widget(self.feedback_icon)
    
    def _adjust_text_wrapping(self, instance, value):
        """Ajusta o quebra-texto do rótulo de mensagem."""
        instance.text_size = instance.size
    
    def _validate_input(self, instance):
        """Valida se os campos obrigatórios foram preenchidos."""
        if not self.name_input.text.strip():
            self._update_message_display(
                "[color=ff0000]ERRO: Nome vazio![/color]", 
                Colors.ERROR_COLOR, 
                "error.png"
            )
        elif not self.age_input.text.strip():
            self._update_message_display(
                "[color=ff0000]ERRO: Idade vazia![/color]", 
                Colors.ERROR_COLOR, 
                "error.png"
            )
        else:
            self._update_message_display("", (0, 0, 0, 1), "")
    
    def _update_message_display(self, message, color, icon_path):
        """Atualiza a mensagem e ícone de feedback."""
        self.message_label.text = message
        self.message_label.color = color
        self.feedback_icon.source = icon_path
        self.feedback_icon.opacity = 1 if icon_path else 0
    
    def _verify_age(self, instance):
        """Verifica a faixa etária baseada na idade fornecida."""
        name = self.name_input.text.strip()
        age_text = self.age_input.text.strip()
        
        if not name or not age_text:
            self._update_message_display(
                "[color=ff0000]Por favor, preencha todos os campos.[/color]", 
                Colors.ERROR_COLOR, 
                "error.png"
            )
            return
        
        try:
            age = int(age_text)
        except ValueError:
            self._update_message_display(
                "[color=ff0000]Digite apenas números.[/color]", 
                Colors.ERROR_COLOR, 
                "error.png"
            )
            return
        
        self._determine_age_category(name, age)
    
    def _determine_age_category(self, name, age):
        """Determina e exibe a categoria etária com mensagens temáticas."""
        if age < 13:
            self._update_message_display(
                f"[color=ffff00]Olá, {name}! Você é uma CRIANÇA.[/color]", 
                Colors.WARNING_COLOR, 
                "warning.png"
            )
        elif age < 18:
            self._update_message_display(
                f"[color=ff00ff]Olá, {name}! Você é um ADOLESCENTE.[/color]", 
                Colors.WARNING_COLOR, 
                "warning.png"
            )
        elif age < 30:
            self._update_message_display(
                f"[color=00ff00]Olá, {name}! Você é um JOVEM ADULTO.[/color]", 
                Colors.SUCCESS_COLOR, 
                "success.png"
            )
        elif age < 60:
            self._update_message_display(
                f"[color=00ffff]Olá, {name}! Você é um ADULTO.[/color]", 
                Colors.SUCCESS_COLOR, 
                "success.png"
            )
        else:
            self._update_message_display(
                f"[color=00aaff]Olá, {name}! Você é um IDOSO :D[/color]", 
                Colors.INFO_COLOR, 
                "info.png"
            )


class AgeVerificationApp(App):
    """Aplicativo principal de verificação de idade."""
    
    def build(self):
        """Constrói a interface do aplicativo."""
        Window.clearcolor = Colors.BACKGROUND
        return AgeVerificationForm()


if __name__ == "__main__":
    AgeVerificationApp().run()
```