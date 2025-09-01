import random
import os

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, RoundedRectangle
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView
from kivy.uix.image import Image
from kivy.uix.togglebutton import ToggleButton
from kivy.core.window import Window


# --- Classe visual de Card ---
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


# --- Lógica de Sorteio ---
class FilmeSorteador:
    def __init__(self):
        self.filmes = {
            "Ação": [("Mad Max: Estrada da Fúria", 2015, "mad_max.jpg"),
                     ("John Wick", 2014, "john_wick.jpg"),
                     ("Duro de Matar", 1988, "duro_de_matar.jpg")],
            "Comédia": [("Superbad", 2007, "superbad.png"),
                        ("As Branquelas", 2004, "branquelas.jpeg")],
            "Animação": [("Toy Story", 1995, "toy_story.webp"),
                         ("Shrek", 2001, "shrek.jpg")]
        }
        self.idade_limite = {
            "Ação": (16, 100),
            "Comédia": (10, 100),
            "Animação": (0, 100)
        }

    def sortear_filme(self, genero):
        if genero in self.filmes:
            return random.choice(self.filmes[genero])
        return None


# --- Tela 1: Boas-Vindas ---
class WelcomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation="vertical", padding=20, spacing=10)

        self.name_input = TextInput(hint_text="Digite seu nome")
        self.age_input = TextInput(hint_text="Digite sua idade", input_filter="int")

        btn_continue = Button(text="Continuar", size_hint=(1, 0.3))
        btn_continue.bind(on_press=self.go_to_suggestion)

        layout.add_widget(Label(text="Bem-vindo ao ASFApp!", font_size=24))
        layout.add_widget(self.name_input)
        layout.add_widget(self.age_input)
        layout.add_widget(btn_continue)

        self.add_widget(layout)

    def go_to_suggestion(self, instance):
        app = App.get_running_app()
        app.user_name = self.name_input.text.strip()
        app.user_age = self.age_input.text.strip()
        app.sm.current = "suggestion"


# --- Tela 2: Sugestão de Filmes ---
class SuggestionScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        Window.clearcolor = (0.1, 0.1, 0.1, 1)
        self.sorteador = FilmeSorteador()

        self.card = Card(orientation="vertical", padding=20, spacing=15,
                         size_hint=(0.9, 0.85), pos_hint={"center_x": 0.5, "center_y": 0.5})

        # Mensagem de boas-vindas
        self.title_label = Label(text="", font_size=22, bold=True, color=(0, 1, 0.6, 1))
        self.card.add_widget(self.title_label)

        # Botões de seleção de gênero
        self.genre_buttons = BoxLayout(size_hint=(1, 0.15), spacing=10)
        self.genres = ["Ação", "Comédia", "Animação"]
        self.toggle_buttons = {}

        for genre in self.genres:
            btn = ToggleButton(text=genre, group='genres', size_hint=(1, 1))
            self.toggle_buttons[genre] = btn
            self.genre_buttons.add_widget(btn)

        self.card.add_widget(self.genre_buttons)

        # Botão sugerir
        self.button = Button(text=" GERAR FILME ", size_hint=(1, 0.2),
                             background_normal='', background_color=(0, 0.8, 0.4, 1),
                             font_size=20, color=(0, 0, 0, 1))
        self.button.bind(on_press=self.sugerir_filme)
        self.card.add_widget(self.button)

        # Label de saída
        self.message_label = Label(text="", font_size=20,
                                   halign="center", valign="middle", size_hint=(1, 0.4),
                                   color=(1, 0, 1, 1), markup=True)
        self.message_label.bind(size=self.ajustar_texto)
        self.card.add_widget(self.message_label)

        # Histórico
        self.history_scroll = ScrollView(size_hint=(1, None), height=0)
        self.history_box = BoxLayout(orientation='vertical', size_hint_y=None, spacing=10, padding=5)
        self.history_box.bind(minimum_height=self.history_box.setter('height'))
        self.history_scroll.add_widget(self.history_box)
        self.card.add_widget(self.history_scroll)

        self.add_widget(self.card)

    def on_enter(self, *args):
        app = App.get_running_app()
        self.title_label.text = f"Olá, {app.user_name}! Escolha um gênero de filme:"

    def ajustar_texto(self, instance, value):
        instance.text_size = instance.size

    def sugerir_filme(self, instance):
        app = App.get_running_app()
        nome = app.user_name
        idade_texto = app.user_age
        genero = next((genre for genre, btn in self.toggle_buttons.items() if btn.state == 'down'), None)

        if not idade_texto.isdigit():
            self.show_popup("ERRO: Digite uma idade válida!")
            return

        idade = int(idade_texto)
        min_idade, max_idade = self.sorteador.idade_limite.get(genero, (0, 100))
        if idade < min_idade or idade > max_idade:
            self.show_popup(f"ERRO: Idade não permitida para {genero}.")
            return

        filme = self.sorteador.sortear_filme(genero)
        if filme:
            self.message_label.text = (
                f"[b][color=00ff99]Olá, {nome}![/color][/b]\n"
                f"Sua sugestão de filme de {genero} é:\n"
                f"[color=ff00ff]{filme[0]} ({filme[1]})[/color]"
            )
            self.history_box.add_widget(Label(text=f"{nome} viu {filme[0]} ({filme[1]})", size_hint_y=None, height=30))
            self.history_scroll.height = min(300, self.history_box.height)

    def show_popup(self, message):
        popup = Popup(title='Mensagem', content=Label(text=message), size_hint=(0.8, 0.4))
        popup.open()


# --- Gerenciador de Telas ---
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
