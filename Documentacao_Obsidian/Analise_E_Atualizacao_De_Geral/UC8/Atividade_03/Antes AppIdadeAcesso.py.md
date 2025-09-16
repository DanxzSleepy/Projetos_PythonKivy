```python

from kivy.app import App

from kivy.uix.boxlayout import BoxLayout

from kivy.uix.label import Label

from kivy.uix.button import Button

from kivy.uix.textinput import TextInput

from kivy.core.window import Window

from kivy.uix.image import Image

  

#  Paleta retrô neon

class Colors:

    BACKGROUND = (0, 0, 0, 1)  # fundo preto terminal

    TITLE_COLOR = (0, 1, 0.6, 1)  # verde neon

    BUTTON_COLOR = (1, 0.2, 0.8, 1)  # rosa neon

    ERROR_COLOR = (1, 0, 0, 1)  # vermelho

    WARNING_COLOR = (1, 1, 0, 1)  # amarelo forte

    INFO_COLOR = (0.3, 0.8, 1, 1)  # azul neon

    SUCCESS_COLOR = (0, 1, 0, 1)  # verde neon brilhante

  
  

class AgeForm(BoxLayout):

    def __init__(self, **kwargs):

        super().__init__(orientation="vertical", padding=20, spacing=15, **kwargs)

  

        # Título retrô

        self.title_label = Label(

            text=" IDADE - Verificador de Faixa Etária ",

            font_size=28,

            bold=True,

            color=Colors.TITLE_COLOR,

            size_hint=(1, 0.2)

        )

        self.add_widget(self.title_label)

  

        # Campo Nome estilo terminal

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

  

        # Campo Idade estilo terminal

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

        self.age_input.bind(on_text_validate=self.validate_input)

        self.add_widget(self.age_input)

  

        # Botão neon

        self.button = Button(

            text=" VERIFICAR ",

            size_hint=(1, 0.2),

            background_normal='',

            background_color=Colors.BUTTON_COLOR,

            font_size=20,

            color=(0, 0, 0, 1)  # texto preto p/ contraste

        )

        self.button.bind(on_press=self.verify_age)

        self.add_widget(self.button)

  

        # Mensagem final com estilo CRT

        self.message_label = Label(

            text="",

            font_size=20,

            halign="center",

            valign="middle",

            size_hint=(1, 0.3),

            color=Colors.SUCCESS_COLOR,

            markup=True

        )

        self.message_label.bind(size=self.adjust_text)

        self.add_widget(self.message_label)

  

        # Ícone de feedback

        self.feedback_icon = Image(size_hint=(None, None), size=(50, 50))

        self.add_widget(self.feedback_icon)

  

    def adjust_text(self, instance, value):

        instance.text_size = instance.size

  

    def validate_input(self, instance):

        if not self.name_input.text.strip():

            self.update_message("[color=ff0000]ERRO: Nome vazio![/color]", Colors.ERROR_COLOR, "error.png")

        elif not self.age_input.text.strip():

            self.update_message("[color=ff0000]ERRO: Idade vazia![/color]", Colors.ERROR_COLOR, "error.png")

        else:

            self.update_message("", (0, 0, 0, 1), "")

  

    def update_message(self, message, color, icon_path):

        self.message_label.text = message

        self.message_label.color = color

        self.feedback_icon.source = icon_path

        self.feedback_icon.opacity = 1 if icon_path else 0

  

    def verify_age(self, instance):

        nome = self.name_input.text.strip()

        idade_texto = self.age_input.text.strip()

  

        if not nome or not idade_texto:

            self.update_message("[color=ff0000]Por favor, preencha todos os campos.[/color]", Colors.ERROR_COLOR, "error.png")

            return

  

        try:

            idade = int(idade_texto)

        except ValueError:

            self.update_message("[color=ff0000]Digite apenas números.[/color]", Colors.ERROR_COLOR, "error.png")

            return

  

        # Estilo retrô nas mensagens

        if idade < 13:

            self.update_message(f"[color=ffff00]Olá, {nome}! Você é uma CRIANÇA.[/color]", Colors.WARNING_COLOR, "warning.png")

        elif idade < 18:

            self.update_message(f"[color=ff00ff]Olá, {nome}! Você é um ADOLESCENTE.[/color]", Colors.WARNING_COLOR, "warning.png")

        elif idade < 30:

            self.update_message(f"[color=00ff00]Olá, {nome}! Você é um JOVEM ADULTO.[/color]", Colors.SUCCESS_COLOR, "success.png")

        elif idade < 60:

            self.update_message(f"[color=00ffff]Olá, {nome}! Você é um ADULTO.[/color]", Colors.SUCCESS_COLOR, "success.png")

        else:

            self.update_message(f"[color=00aaff]Olá, {nome}! Você é um IDOSO :D[/color]", Colors.INFO_COLOR, "info.png")

  
  

class IdadeApp(App):

    def build(self):

        Window.clearcolor = Colors.BACKGROUND

        return AgeForm()

  
  

if __name__ == "__main__":

    IdadeApp().run()

```