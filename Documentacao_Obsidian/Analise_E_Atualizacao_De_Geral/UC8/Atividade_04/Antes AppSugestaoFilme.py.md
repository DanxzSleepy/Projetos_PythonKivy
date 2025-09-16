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

from kivy.uix.gridlayout import GridLayout

from kivy.uix.togglebutton import ToggleButton

  
  

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

  

        # Limites de idade para cada gênero

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

  
  

class FilmeApp(App):

    def build(self):

        Window.clearcolor = (0.1, 0.1, 0.1, 1)

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

  

        self.age_input = TextInput(

            hint_text="Digite sua idade...",

            multiline=False,

            size_hint=(1, 0.15),

            background_color=(0, 0, 0, 1),

            foreground_color=(0, 1, 0, 1),

            cursor_color=(1, 0, 1, 1),

            font_size=18

        )

        self.card.add_widget(self.age_input)

  

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

  

        # ScrollView para histórico de sugestões (só aparece quando há conteúdo)

        self.history_scroll = ScrollView(size_hint=(1, None), height=0)

        self.history_box = BoxLayout(orientation='vertical', size_hint_y=None, spacing=10, padding=5)

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

  

    def validar_entrada(self, nome, idade_texto, genero):

        if not nome or len(nome) > 50 or not nome.isalnum():

            self.show_popup("ERRO: Digite um nome válido (máx. 50 caracteres, sem caracteres especiais)!")

            return False

        if not idade_texto.isdigit() or int(idade_texto) < 0:

            self.show_popup("ERRO: Digite uma idade válida!")

            return False

        if genero is None:

            self.show_popup("ERRO: Selecione um gênero!")

            return False

        idade = int(idade_texto)

        min_idade, max_idade = self.sorteador.idade_limite[genero]

        if idade < min_idade or idade > max_idade:

            self.show_popup(f"ERRO: Idade deve estar entre {min_idade} e {max_idade} para o gênero {genero}.")

            return False

        return True

  

    def sugerir_filme(self, instance):

        nome = self.name_input.text.strip()

        idade_texto = self.age_input.text.strip()

        genero = next((genre for genre, btn in self.toggle_buttons.items() if btn.state == 'down'), None)

  

        if not self.validar_entrada(nome, idade_texto, genero):

            return

  

        filme_escolhido = self.sorteador.sortear_filme(genero)

        if filme_escolhido:

            self.message_label.text = (

                f"[b][color=00ff99]Olá, {nome}![/color][/b]\n"

                f"Sua sugestão de filme de {genero} é:\n"

                f"[color=ff00ff]{filme_escolhido[0]} ({filme_escolhido[1]})[/color]"

            )

        # Adiciona a sugestão ao histórico com imagem

            img_path = os.path.join(os.path.dirname(__file__), filme_escolhido[2])

            # Debug: verifica se o arquivo existe

            if not os.path.exists(img_path):

                print(f"ERRO: Arquivo não encontrado: {img_path}")

                # Adiciona apenas o texto se a imagem não existir

                self.history_box.add_widget(Label(

                    text=f"{nome} sugeriu: {filme_escolhido[0]} ({filme_escolhido[1]}) - [Imagem não encontrada]",

                    color=(1, 1, 1, 1),

                    size_hint_y=None,

                    height=30

                ))

            else:

                print(f"Imagem encontrada: {img_path}")

                img = Image(

                    source=img_path,

                    size_hint=(1, None),

                    height=200,

                    allow_stretch=True  # Permite redimensionamento

                )

                label = Label(

                    text=f"{nome} sugeriu: {filme_escolhido[0]} ({filme_escolhido[1]})",

                    color=(1, 1, 1, 1),

                    size_hint_y=None,

                    height=30

                )

                self.history_box.add_widget(label)

                self.history_box.add_widget(img)

  

            # Expande o ScrollView para mostrar o histórico

            self.history_scroll.height = min(300, self.history_box.height)

            # Scroll automático para a última entrada

            self.history_scroll.scroll_to(self.history_box.children[0])

  

    def limpar_campos(self, instance):

        self.name_input.text = ""

        self.age_input.text = ""

        for btn in self.toggle_buttons.values():

            btn.state = 'normal'

        self.message_label.text = ""

        self.history_box.clear_widgets()  # Limpa o histórico

  

if __name__ == "__main__":

    FilmeApp().run()

```