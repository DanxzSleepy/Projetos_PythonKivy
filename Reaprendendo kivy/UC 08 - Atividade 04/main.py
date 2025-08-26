import random
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, RoundedRectangle


class Card(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas.before:
            # Fundo preto neon
            Color(0.05, 0.05, 0.05, 1)
            self.bg = RoundedRectangle(radius=[15], pos=self.pos, size=self.size)
        self.bind(pos=self.update_bg, size=self.update_bg)

    def update_bg(self, *args):
        self.bg.pos = self.pos
        self.bg.size = self.size


class FilmeApp(App):
    def build(self):
        # Fundo preto com vibe retrô
        Window.clearcolor = (0, 0, 0, 1)

        # Lista de filmes
        self.filmes = [
            "Matrix (1999)", "Toy Story (1995)", "Avatar (2009)", "O Rei Leão (1994)",
            "Homem-Aranha (2002)", "Interestelar (2014)", "Shrek (2001)", "Clube da Luta (1999)",
            "Procurando Nemo (2003)", "Vingadores: Ultimato (2019)", "Jurassic Park (1993)",
            "Gladiador (2000)", "O Senhor dos Anéis: A Sociedade do Anel (2001)",
            "O Senhor dos Anéis: O Retorno do Rei (2003)", "Batman: O Cavaleiro das Trevas (2008)",
            "Forrest Gump (1994)", "Titanic (1997)", "Star Wars: Uma Nova Esperança (1977)",
            "Star Wars: O Império Contra-Ataca (1980)", "De Volta para o Futuro (1985)",
            "Harry Potter e a Pedra Filosofal (2001)", "Piratas do Caribe: A Maldição do Pérola Negra (2003)",
            "Pantera Negra (2018)", "A Origem (2010)", "Homem de Ferro (2008)",
            "Divertida Mente (2015)", "Coringa (2019)", "A Bela e a Fera (1991)",
            "Os Incríveis (2004)", "O Exterminador do Futuro 2 (1991)"
        ]

        root = FloatLayout()

        # Cartão retrô central
        self.card = Card(
            orientation="vertical",
            padding=20,
            spacing=15,
            size_hint=(0.9, 0.75),
            pos_hint={"center_x": 0.5, "center_y": 0.5}
        )

        # Título estilo neon
        self.title_label = Label(
            text=" A.S.F.A. - App de Sugestão de Filmes Aaleatorios ",
            font_size=24,
            bold=True,
            color=(0, 1, 0.6, 1),  # verde neon
            size_hint=(1, 0.2)
        )
        self.card.add_widget(self.title_label)

        # Input nome estilo terminal
        self.name_input = TextInput(
            hint_text="Digite seu nome...",
            multiline=False,
            size_hint=(1, 0.15),
            background_color=(0, 0, 0, 1),
            foreground_color=(0, 1, 0, 1),  # verde neon
            cursor_color=(1, 0, 1, 1),  # rosa neon
            font_size=18
        )
        self.card.add_widget(self.name_input)

        # Botão retrô
        self.button = Button(
            text=" GERAR FILME ",
            size_hint=(1, 0.2),
            background_normal='',
            background_color=(0, 0.8, 0.4, 1),  # verde neon
            font_size=20,
            color=(0, 0, 0, 1)  # texto preto
        )
        self.button.bind(on_press=self.sugerir_filme)
        self.card.add_widget(self.button)

        # Mensagem final estilo CRT
        self.message_label = Label(
            text="",
            font_size=20,
            halign="center",
            valign="middle",
            size_hint=(1, 0.4),
            color=(1, 0, 1, 1),  # rosa neon
            markup=True
        )
        self.message_label.bind(size=self.ajustar_texto)
        self.card.add_widget(self.message_label)

        root.add_widget(self.card)
        return root

    def ajustar_texto(self, instance, value):
        instance.text_size = instance.size

    def sugerir_filme(self, instance):
        nome = self.name_input.text.strip()

        if not nome:
            self.message_label.text = "[color=ff0000]ERRO: Digite seu nome primeiro![/color]"
            return

        filme_escolhido = random.choice(self.filmes)
        self.message_label.text = (
            f"[b][color=00ff99]Olá, {nome}![/color][/b]\n"
            f"Sua sugestão retrô é:\n"
            f"[color=ff00ff]{filme_escolhido}[/color]"
        )


if __name__ == "__main__":
    FilmeApp().run()