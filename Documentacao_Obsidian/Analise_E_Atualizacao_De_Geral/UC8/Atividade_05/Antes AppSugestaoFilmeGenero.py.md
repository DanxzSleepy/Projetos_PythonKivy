```python
import random

from kivy.app import App

from kivy.uix.boxlayout import BoxLayout

from kivy.uix.label import Label

from kivy.uix.button import Button

from kivy.uix.textinput import TextInput

from kivy.core.window import Window

from kivy.uix.floatlayout import FloatLayout

from kivy.graphics import Color, RoundedRectangle

from kivy.uix.togglebutton import ToggleButton

from kivy.uix.popup import Popup

from kivy.uix.scrollview import ScrollView

  
  

class Card(BoxLayout):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)

        with self.canvas.before:

            Color(0.05, 0.05, 0.05, 1)

            self.bg = RoundedRectangle(radius=[15], pos=self.pos, size=self.size)

        self.bind(pos=self.update_bg, size=self.update_bg)

  

    def update_bg(self, *args):

        self.bg.pos = self.pos

        self.bg.size = self.size

  
  

class FilmeSorteador:

    def __init__(self):

        self.filmes = {

            "Ação": [

                ("Mad Max: Estrada da Fúria", 2015),

                ("John Wick", 2014),

                ("Duro de Matar", 1988),

                ("Os Vingadores", 2012),

                ("Gladiador", 2000),

            ],

            "Comédia": [

                ("Superbad", 2007),

                ("A Morte Lhe Cai Bem", 1992),

                ("Os Caça-Fantasmas", 1984),

                ("O Diário de uma Princesa", 2001),

                ("As Branquelas", 2004),

            ],

            "Drama": [

                ("Forrest Gump", 1994),

                ("O Poderoso Chefão", 1972),

                ("A Lista de Schindler", 1993),

                ("Clube da Luta", 1999),

                ("O Senhor dos Anéis: O Retorno do Rei", 2003),

            ],

            "Ficção Científica": [

                ("Interestelar", 2014),

                ("Blade Runner 2049", 2017),

                ("A Origem", 2010),

                ("Ex Machina", 2014),

                ("Matrix", 1999),

            ],

            "Animação": [

                ("Toy Story", 1995),

                ("Procurando Nemo", 2003),

                ("O Rei Leão", 1994),

                ("Shrek", 2001),

                ("Divertida Mente", 2015),

            ]

        }

  

    def sortear_filme(self, genero):

        if genero in self.filmes:

            return random.choice(self.filmes[genero])

        return None

  
  

class FilmeApp(App):

    def build(self):

        Window.clearcolor = (0, 0, 0, 1)

        self.sorteador = FilmeSorteador()

  

        root = FloatLayout()

  

        self.card = Card(

            orientation="vertical",

            padding=20,

            spacing=15,

            size_hint=(0.9, 0.75),

            pos_hint={"center_x": 0.5, "center_y": 0.5}

        )

  

        self.title_label = Label(

            text=" A.S.F.A. - App de Sugestão de Filmes Aleatórios ",

            font_size=24,

            bold=True,

            color=(0, 1, 0.6, 1),

            size_hint=(1, 0.2)

        )

        self.card.add_widget(self.title_label)

  

        self.name_input = TextInput(

            hint_text="Digite seu nome...",

            multiline=False,

            size_hint=(1, 0.15),

            background_color=(0, 0, 0, 1),

            foreground_color=(0, 1, 0, 1),

            cursor_color=(1, 0, 1, 1),

            font_size=18

        )

        self.card.add_widget(self.name_input)

  

        # Botões de seleção de gênero

        self.genre_buttons = BoxLayout(size_hint=(1, 0.15), spacing=10)

        self.genres = ["Ação", "Comédia", "Drama", "Ficção Científica", "Animação"]

        self.toggle_buttons = {}

  

        for genre in self.genres:

            btn = ToggleButton(text=genre, group='genres', size_hint=(1, 1))

            self.toggle_buttons[genre] = btn

            self.genre_buttons.add_widget(btn)

  

        self.card.add_widget(self.genre_buttons)

  

        self.button = Button(

            text=" GERAR FILME ",

            size_hint=(1, 0.2),

            background_normal='',

            background_color=(0, 0.8, 0.4, 1),

            font_size=20,

            color=(0, 0, 0, 1)

        )

        self.button.bind(on_press=self.sugerir_filme)

        self.card.add_widget(self.button)

  

        # Botão Limpar

        self.clear_button = Button(

            text=" LIMPAR ",

            size_hint=(1, 0.2),

            background_normal='',

            background_color=(1, 0, 0, 1),  # vermelho

            font_size=20,

            color=(1, 1, 1, 1)

        )

        self.clear_button.bind(on_press=self.limpar_campos)

        self.card.add_widget(self.clear_button)

  

        # Mensagem final estilo CRT

        self.message_label = Label(

            text="",

            font_size=20,

            halign="center",

            valign="middle",

            size_hint=(1, 0.4),

            color=(1, 0, 1, 1),  # rosa neon

            markup=True

        )

        self.message_label.bind(size=self.ajustar_texto)

        self.card.add_widget(self.message_label)

  

        # ScrollView para histórico de sugestões

        self.history_scroll = ScrollView(size_hint=(1, 0.4))

        self.history_box = BoxLayout(orientation='vertical', size_hint_y=None)

        self.history_box.bind(minimum_height=self.history_box.setter('height'))

        self.history_scroll.add_widget(self.history_box)

  

        self.card.add_widget(self.history_scroll)

  

        root.add_widget(self.card)

        return root

  

    def show_popup(self, message):

        popup = Popup(title='Mensagem', content=Label(text=message), size_hint=(0.8, 0.4))

        popup.open()

  

    def ajustar_texto(self, instance, value):

        instance.text_size = instance.size

  

    def validar_entrada(self, nome):

        if not nome:

            self.show_popup("ERRO: Digite seu nome primeiro!")

            return False

        return True

  

    def sugerir_filme(self, instance):

        nome = self.name_input.text.strip()

        genero = next((genre for genre, btn in self.toggle_buttons.items() if btn.state == 'down'), None)

  

        if not self.validar_entrada(nome):

            return

  

        if not genero:

            self.show_popup("ERRO: Selecione um gênero!")

            return

  

        filme_escolhido = self.sorteador.sortear_filme(genero)

        if filme_escolhido:

            self.message_label.text = (

                f"[b][color=00ff99]Olá, {nome}![/color][/b]\n"

                f"Sua sugestão de filme de {genero} é:\n"

                f"[color=ff00ff]{filme_escolhido[0]} ({filme_escolhido[1]})[/color]"

            )

            # Adiciona a sugestão ao histórico

            self.history_box.add_widget(Label(text=f"{nome} sugeriu: {filme_escolhido[0]} ({filme_escolhido[1]})", color=(1, 1, 1, 1)))

  

    def limpar_campos(self, instance):

        self.name_input.text = ""

        for btn in self.toggle_buttons.values():

            btn.state = 'normal'

        self.message_label.text = ""

  

if __name__ == "__main__":

    FilmeApp().run()
```