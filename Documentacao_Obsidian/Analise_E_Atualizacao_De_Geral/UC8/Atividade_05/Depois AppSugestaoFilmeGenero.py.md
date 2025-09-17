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


class RoundedCard(BoxLayout):
    """Widget personalizado com fundo arredondado estilo cartão."""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._setup_background()
    
    def _setup_background(self):
        """Configura o fundo arredondado do cartão."""
        with self.canvas.before:
            Color(0.05, 0.05, 0.05, 1)
            self.background = RoundedRectangle(radius=[15], pos=self.pos, size=self.size)
        self.bind(pos=self._update_background, size=self._update_background)
    
    def _update_background(self, *args):
        """Atualiza a posição e tamanho do fundo quando o widget é redimensionado."""
        self.background.pos = self.pos
        self.background.size = self.size


class MovieSuggester:
    """Classe responsável por gerenciar o catálogo de filmes e sugerir aleatoriamente."""
    
    def __init__(self):
        self.movies = self._initialize_movie_catalog()
    
    def _initialize_movie_catalog(self):
        """Inicializa o catálogo de filmes organizado por gênero."""
        return {
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
    
    def suggest_movie(self, genre):
        """Sugere aleatoriamente um filme do gênero especificado."""
        if genre in self.movies:
            return random.choice(self.movies[genre])
        return None


class MovieSuggestionApp(App):
    """Aplicativo principal de sugestão de filmes por gênero."""
    
    def build(self):
        """Constrói a interface gráfica do aplicativo."""
        Window.clearcolor = (0, 0, 0, 1)
        self.suggester = MovieSuggester()
        
        root_layout = FloatLayout()
        self._setup_main_card(root_layout)
        
        return root_layout
    
    def _setup_main_card(self, root_layout):
        """Configura o cartão principal com todos os componentes da interface."""
        self.main_card = RoundedCard(
            orientation="vertical",
            padding=20,
            spacing=15,
            size_hint=(0.9, 0.75),
            pos_hint={"center_x": 0.5, "center_y": 0.5}
        )
        
        self._create_title_label()
        self._create_name_input()
        self._create_genre_buttons()
        self._create_action_buttons()
        self._create_message_label()
        self._create_history_section()
        
        root_layout.add_widget(self.main_card)
    
    def _create_title_label(self):
        """Cria o rótulo de título do aplicativo."""
        self.title_label = Label(
            text="A.S.F.A. - App de Sugestão de Filmes Aleatórios",
            font_size=24,
            bold=True,
            color=(0, 1, 0.6, 1),
            size_hint=(1, 0.2)
        )
        self.main_card.add_widget(self.title_label)
    
    def _create_name_input(self):
        """Cria o campo de entrada para o nome do usuário."""
        self.name_input = TextInput(
            hint_text="Digite seu nome...",
            multiline=False,
            size_hint=(1, 0.15),
            background_color=(0, 0, 0, 1),
            foreground_color=(0, 1, 0, 1),
            cursor_color=(1, 0, 1, 1),
            font_size=18
        )
        self.main_card.add_widget(self.name_input)
    
    def _create_genre_buttons(self):
        """Cria os botões de seleção de gênero cinematográfico."""
        self.genre_buttons_layout = BoxLayout(size_hint=(1, 0.15), spacing=10)
        self.genres = ["Ação", "Comédia", "Drama", "Ficção Científica", "Animação"]
        self.toggle_buttons = {}
        
        for genre in self.genres:
            button = ToggleButton(text=genre, group='genres', size_hint=(1, 1))
            self.toggle_buttons[genre] = button
            self.genre_buttons_layout.add_widget(button)
        
        self.main_card.add_widget(self.genre_buttons_layout)
    
    def _create_action_buttons(self):
        """Cria os botões de ação (gerar filme e limpar)."""
        self.generate_button = Button(
            text="GERAR FILME",
            size_hint=(1, 0.2),
            background_normal='',
            background_color=(0, 0.8, 0.4, 1),
            font_size=20,
            color=(0, 0, 0, 1)
        )
        self.generate_button.bind(on_press=self._suggest_movie)
        self.main_card.add_widget(self.generate_button)
        
        self.clear_button = Button(
            text="LIMPAR",
            size_hint=(1, 0.2),
            background_normal='',
            background_color=(1, 0, 0, 1),
            font_size=20,
            color=(1, 1, 1, 1)
        )
        self.clear_button.bind(on_press=self._clear_fields)
        self.main_card.add_widget(self.clear_button)
    
    def _create_message_label(self):
        """Cria o rótulo para exibir mensagens e sugestões."""
        self.message_label = Label(
            text="",
            font_size=20,
            halign="center",
            valign="middle",
            size_hint=(1, 0.4),
            color=(1, 0, 1, 1),
            markup=True
        )
        self.message_label.bind(size=self._adjust_text_wrapping)
        self.main_card.add_widget(self.message_label)
    
    def _create_history_section(self):
        """Cria a seção de histórico de sugestões."""
        self.history_scroll = ScrollView(size_hint=(1, 0.4))
        self.history_container = BoxLayout(
            orientation='vertical', 
            size_hint_y=None
        )
        self.history_container.bind(minimum_height=self.history_container.setter('height'))
        self.history_scroll.add_widget(self.history_container)
        self.main_card.add_widget(self.history_scroll)
    
    def _show_popup(self, title, message):
        """Exibe um popup com uma mensagem para o usuário."""
        popup = Popup(title=title, content=Label(text=message), size_hint=(0.8, 0.4))
        popup.open()
    
    def _adjust_text_wrapping(self, instance, value):
        """Ajusta o quebra-texto do rótulo de mensagem."""
        instance.text_size = instance.size
    
    def _validate_input(self, name, selected_genre):
        """Valida os dados de entrada do usuário."""
        if not name:
            self._show_popup("Erro de Validação", "Digite seu nome primeiro!")
            return False
        
        if not selected_genre:
            self._show_popup("Erro de Validação", "Selecione um gênero!")
            return False
        
        return True
    
    def _suggest_movie(self, instance):
        """Processa a solicitação de sugestão de filme."""
        name = self.name_input.text.strip()
        selected_genre = next((genre for genre, btn in self.toggle_buttons.items() 
                              if btn.state == 'down'), None)
        
        if not self._validate_input(name, selected_genre):
            return
        
        suggested_movie = self.suggester.suggest_movie(selected_genre)
        if suggested_movie:
            self._display_movie_suggestion(name, selected_genre, suggested_movie)
            self._add_to_history(name, suggested_movie)
    
    def _display_movie_suggestion(self, name, genre, movie):
        """Exibe a sugestão de filme na interface."""
        movie_title, movie_year = movie
        self.message_label.text = (
            f"[b][color=00ff99]Olá, {name}![/color][/b]\n"
            f"Sua sugestão de filme de {genre} é:\n"
            f"[color=ff00ff]{movie_title} ({movie_year})[/color]"
        )
    
    def _add_to_history(self, name, movie):
        """Adiciona a sugestão atual ao histórico."""
        movie_title, movie_year = movie
        history_label = Label(
            text=f"{name} sugeriu: {movie_title} ({movie_year})",
            color=(1, 1, 1, 1),
            size_hint_y=None,
            height=30
        )
        self.history_container.add_widget(history_label)
    
    def _clear_fields(self, instance):
        """Limpa todos os campos e o histórico."""
        self.name_input.text = ""
        for button in self.toggle_buttons.values():
            button.state = 'normal'
        self.message_label.text = ""
        self.history_container.clear_widgets()


if __name__ == "__main__":
    MovieSuggestionApp().run()
```