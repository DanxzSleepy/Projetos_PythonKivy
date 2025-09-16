```python
import random

import os

from kivy.app import App

from kivy.uix.boxlayout import BoxLayout

from kivy.uix.label import Label

from kivy.uix.button import Button

from kivy.uix.textinput import TextInput

from kivy.core.window import Window

from kivy.uix.floatlayout import FloatLayout

from kivy.graphics import Color, RoundedRectangle

from kivy.uix.popup import Popup

from kivy.uix.scrollview import ScrollView

from kivy.uix.image import Image

from kivy.uix.togglebutton import ToggleButton

from kivy.uix.screenmanager import ScreenManager, Screen

  
  

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

                ("Mad Max: Estrada da Fúria", 2015, "mad_max.jpg"),

                ("John Wick", 2014, "john_wick.jpg"),

                ("Duro de Matar", 1988, "duro_de_matar.jpg"),

                ("Os Vingadores", 2012, "vingadores.jpg"),

                ("Gladiador", 2000, "gladiador.jpg"),

            ],

            "Comédia": [

                ("Superbad", 2007, "superbad.png"),

                ("A Morte Lhe Cai Bem", 1992, "morte_lhe_cai_bem.jpg"),

                ("Os Caça-Fantasmas", 1984, "caca_fantasmas.jpg"),

                ("O Diário de uma Princesa", 2001, "diario_princesa.webp"),

                ("As Branquelas", 2004, "branquelas.jpeg"),

            ],

            "Drama": [

                ("Forrest Gump", 1994, "forrest_gump.jpg"),

                ("O Poderoso Chefão", 1972, "poderoso_chefa.jpg"),

                ("A Lista de Schindler", 1993, "lista_schindler.jpg"),

                ("Clube da Luta", 1999, "clube_luta.jpg"),

                ("O Senhor dos Anéis: O Retorno do Rei", 2003, "senhor_aneis.jpg"),

            ],

            "Ficção Científica": [

                ("Interestelar", 2014, "interestelar.png"),

                ("Blade Runner 2049", 2017, "blade_runner.jpg"),

                ("A Origem", 2010, "origem.jpg"),

                ("Ex Machina", 2014, "ex_machina.webp"),

                ("Matrix", 1999, "matrix.png"),

            ],

            "Animação": [

                ("Toy Story", 1995, "toy_story.webp"),

                ("Procurando Nemo", 2003, "procurando_nemo.jpg"),

                ("O Rei Leão", 1994, "rei_leao.webp"),

                ("Shrek", 2001, "shrek.jpg"),

                ("Divertida Mente", 2015, "divertida_mente.webp"),

            ]

        }

        self.idade_limite = {

            "Ação": (16, 100),

            "Comédia": (10, 100),

            "Drama": (12, 100),

            "Ficção Científica": (12, 100),

            "Animação": (0, 100)

        }

  

    def sortear_filme(self, genero):

        if genero in self.filmes:

            return random.choice(self.filmes[genero])

        return None

  
  

# --- Tela 1: Boas-vindas ---

class WelcomeScreen(Screen):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)

  

        self.card = Card(orientation="vertical", padding=20, spacing=15,

                         size_hint=(0.9, 0.6), pos_hint={"center_x": 0.5, "center_y": 0.5})

  

        self.card.add_widget(Label(text="Bem-vindo ao ASFApp!", font_size=24, bold=True, color=(0,1,0.6,1)))

  

        self.name_input = TextInput(hint_text="Digite seu nome", size_hint=(1, 0.3))

        self.age_input = TextInput(hint_text="Digite sua idade", input_filter="int", size_hint=(1, 0.3))

  

        btn_continue = Button(text="Continuar", size_hint=(1, 0.3),

                              background_normal='', background_color=(0,0.8,0.4,1),

                              color=(0,0,0,1), font_size=18)

        btn_continue.bind(on_press=self.go_to_suggestion)

  

        self.card.add_widget(self.name_input)

        self.card.add_widget(self.age_input)

        self.card.add_widget(btn_continue)

  

        self.add_widget(self.card)

  

    def go_to_suggestion(self, instance):

        app = App.get_running_app()

        app.user_name = self.name_input.text.strip()

        app.user_age = self.age_input.text.strip()

        app.sm.current = "suggestion"

  
  

# --- Tela 2: Teu app de sugestão completo ---

class SuggestionScreen(Screen):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)

        self.sorteador = FilmeSorteador()

        self.build_ui()

  

    def build_ui(self):

        Window.clearcolor = (0.1, 0.1, 0.1, 1)

        root = FloatLayout()

  

        self.card = Card(orientation="vertical", padding=20, spacing=15,

                         size_hint=(0.9, 0.85), pos_hint={"center_x": 0.5, "center_y": 0.5})

  

        self.title_label = Label(text="", font_size=24, bold=True, color=(0,1,0.6,1), size_hint=(1,0.2))

        self.card.add_widget(self.title_label)

  

        # Gêneros

        self.genre_buttons = BoxLayout(size_hint=(1, 0.15), spacing=10)

        self.genres = list(self.sorteador.filmes.keys())

        self.toggle_buttons = {}

        for genre in self.genres:

            btn = ToggleButton(text=genre, group='genres', size_hint=(1, 1))

            self.toggle_buttons[genre] = btn

            self.genre_buttons.add_widget(btn)

        self.card.add_widget(self.genre_buttons)

  

        # Botão sortear

        self.button = Button(text=" GERAR FILME ", size_hint=(1, 0.2),

                             background_normal='', background_color=(0,0.8,0.4,1),

                             font_size=20, color=(0,0,0,1))

        self.button.bind(on_press=self.sugerir_filme)

        self.card.add_widget(self.button)

  

        # Mensagem

        self.message_label = Label(text="", font_size=20, halign="center", valign="middle",

                                   size_hint=(1, 0.4), color=(1,0,1,1), markup=True)

        self.message_label.bind(size=self.ajustar_texto)

        self.card.add_widget(self.message_label)

  

        # Histórico com scroll

        self.history_scroll = ScrollView(size_hint=(1, None), height=0)

        self.history_box = BoxLayout(orientation='vertical', size_hint_y=None, spacing=10, padding=5)

        self.history_box.bind(minimum_height=self.history_box.setter('height'))

        self.history_scroll.add_widget(self.history_box)

        self.card.add_widget(self.history_scroll)

  

        root.add_widget(self.card)

        self.add_widget(root)

  

    def on_enter(self):

        app = App.get_running_app()

        self.title_label.text = f"Olá, {app.user_name}! Escolha um gênero para receber uma sugestão."

  

    def ajustar_texto(self, instance, value):

        instance.text_size = instance.size

  

    def show_popup(self, message):

        popup = Popup(title='Mensagem', content=Label(text=message), size_hint=(0.8, 0.4))

        popup.open()

  

    def validar_entrada(self, nome, idade_texto, genero):

        if not idade_texto.isdigit():

            self.show_popup("ERRO: Digite uma idade válida!")

            return False

        idade = int(idade_texto)

        min_idade, max_idade = self.sorteador.idade_limite[genero]

        if idade < min_idade or idade > max_idade:

            self.show_popup(f"ERRO: Idade deve estar entre {min_idade} e {max_idade} para {genero}.")

            return False

        return True

  

    def sugerir_filme(self, instance):

        app = App.get_running_app()

        nome = app.user_name

        idade_texto = app.user_age

        genero = next((g for g, btn in self.toggle_buttons.items() if btn.state == 'down'), None)

  

        if not self.validar_entrada(nome, idade_texto, genero):

            return

  

        filme = self.sorteador.sortear_filme(genero)

        if filme:

            self.message_label.text = (

                f"[b][color=00ff99]Olá, {nome}![/color][/b]\n"

                f"Sua sugestão é:\n[color=ff00ff]{filme[0]} ({filme[1]})[/color]"

            )

            img_path = os.path.join(os.path.dirname(__file__), filme[2])

            if os.path.exists(img_path):

                self.history_box.add_widget(Image(source=img_path, size_hint=(1,None), height=200))

            self.history_box.add_widget(Label(text=f"{nome} sugeriu: {filme[0]} ({filme[1]})",

                                              color=(1,1,1,1), size_hint_y=None, height=30))

            self.history_scroll.height = min(300, self.history_box.height)

            self.history_scroll.scroll_to(self.history_box.children[0])

  
  

# --- App principal com ScreenManager ---

class FilmeApp(App):

    def build(self):

        self.user_name = ""

        self.user_age = ""

        self.sm = ScreenManager()

        self.sm.add_widget(WelcomeScreen(name="welcome"))

        self.sm.add_widget(SuggestionScreen(name="suggestion"))

        return self.sm

  
  

if __name__ == "__main__":

    FilmeApp().run()

  
  

# Fim do código
```