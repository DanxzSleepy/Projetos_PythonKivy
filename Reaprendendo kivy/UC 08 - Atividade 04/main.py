import random
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

class FilmeApp(App):
    def build(self):
        # Fundo cinza claro
        Window.clearcolor = (0.95, 0.95, 0.95, 1)

        # Lista de filmes (com ano de lançamento)
        self.filmes = [
            "Matrix (1999)",
            "Toy Story (1995)",
            "Avatar (2009)",
            "O Rei Leão (1994)",
            "Homem-Aranha (2002)",
            "Interestelar (2014)",
            "Shrek (2001)",
            "Clube da Luta (1999)",
            "Procurando Nemo (2003)",
            "Vingadores: Ultimato (2019)"
        ]

        # Layout principal
        self.layout = BoxLayout(orientation="vertical", padding=20, spacing=15)

        # Título
        self.title_label = Label(
            text="🎬 App de Sugestão de Filme 🍿",
            font_size=26,
            bold=True,
            color=(0.2, 0.2, 0.6, 1),
            size_hint=(1, 0.2)
        )
        self.layout.add_widget(self.title_label)

        # Campo Nome
        self.name_input = TextInput(
            hint_text="Digite seu nome",
            multiline=False,
            size_hint=(1, 0.2),
            background_color=(1, 1, 1, 1),
            foreground_color=(0, 0, 0, 1)
        )
        self.layout.add_widget(self.name_input)

        # Botão Sugerir
        self.button = Button(
            text="Sugerir Filme",
            size_hint=(1, 0.2),
            background_normal='',
            background_color=(0.2, 0.6, 0.9, 1),
            font_size=20,
            color=(1, 1, 1, 1)
        )
        self.button.bind(on_press=self.sugerir_filme)
        self.layout.add_widget(self.button)

        # Mensagem final
        self.message_label = Label(
            text="",
            font_size=20,
            halign="center",
            valign="middle",
            size_hint=(1, 0.4),
            color=(0, 0, 0, 1)
        )
        self.message_label.bind(size=self.ajustar_texto)
        self.layout.add_widget(self.message_label)

        return self.layout

    def ajustar_texto(self, instance, value):
        instance.text_size = instance.size

    def sugerir_filme(self, instance):
        nome = self.name_input.text.strip()

        if not nome:
            self.message_label.text = "⚠️ Por favor, digite seu nome."
            self.message_label.color = (1, 0, 0, 1)  # vermelho
            return

        filme_escolhido = random.choice(self.filmes)
        self.message_label.text = f"Olá, {nome}! Sua sugestão de filme é: {filme_escolhido}."
        self.message_label.color = (0, 0.5, 0.2, 1)  # verde

if __name__ == "__main__":
    FilmeApp().run()
