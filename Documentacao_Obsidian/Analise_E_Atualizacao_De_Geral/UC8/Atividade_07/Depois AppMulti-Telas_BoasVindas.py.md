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
        self.age_limits = self._initialize_age_limits()
    
    def _initialize_movie_catalog(self):
        """Inicializa o catálogo de filmes organizado por gênero."""
        return {
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
                ("O Poderoso Chefão", 1972, "poderoso_chefao.jpg"),
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
    
    def _initialize_age_limits(self):
        """Define os limites de idade para cada gênero de filme."""
        return {
            "Ação": (16, 100),
            "Comédia": (10, 100),
            "Drama": (12, 100),
            "Ficção Científica": (12, 100),
            "Animação": (0, 100)
        }
    
    def suggest_movie(self, genre):
        """Sugere aleatoriamente um filme do gênero especificado."""
        if genre in self.movies:
            return random.choice(self.movies[genre])
        return None
    
    def get_age_limits(self, genre):
        """Retorna os limites de idade para um gênero específico."""
        return self.age_limits.get(genre, (0, 100))


class WelcomeScreen(Screen):
    """Tela de boas-vindas para coleta de dados do usuário."""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._setup_ui()
    
    def _setup_ui(self):
        """Configura a interface da tela de boas-vindas."""
        self.card = RoundedCard(
            orientation="vertical", 
            padding=20, 
            spacing=15,
            size_hint=(0.9, 0.6), 
            pos_hint={"center_x": 0.5, "center_y": 0.5}
        )
        
        self._create_welcome_label()
        self._create_input_fields()
        self._create_continue_button()
        
        self.add_widget(self.card)
    
    def _create_welcome_label(self):
        """Cria o rótulo de boas-vindas."""
        welcome_label = Label(
            text="Bem-vindo ao ASFApp!",
            font_size=24, 
            bold=True, 
            color=(0, 1, 0.6, 1)
        )
        self.card.add_widget(welcome_label)
    
    def _create_input_fields(self):
        """Cria os campos de entrada para nome e idade."""
        self.name_input = TextInput(
            hint_text="Digite seu nome", 
            size_hint=(1, 0.3)
        )
        self.age_input = TextInput(
            hint_text="Digite sua idade", 
            input_filter="int", 
            size_hint=(1, 0.3)
        )
        
        self.card.add_widget(self.name_input)
        self.card.add_widget(self.age_input)
    
    def _create_continue_button(self):
        """Cria o botão para continuar para a próxima tela."""
        continue_button = Button(
            text="Continuar", 
            size_hint=(1, 0.3),
            background_normal='', 
            background_color=(0, 0.8, 0.4, 1),
            color=(0, 0, 0, 1), 
            font_size=18
        )
        continue_button.bind(on_press=self._navigate_to_suggestion)
        self.card.add_widget(continue_button)
    
    def _navigate_to_suggestion(self, instance):
        """Navega para a tela de sugestão de filmes."""
        app = App.get_running_app()
        app.user_name = self.name_input.text.strip()
        app.user_age = self.age_input.text.strip()
        app.screen_manager.current = "suggestion"


class SuggestionScreen(Screen):
    """Tela principal de sugestão de filmes."""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.movie_suggester = MovieSuggester()
        self._setup_ui()
    
    def _setup_ui(self):
        """Configura a interface da tela de sugestão."""
        Window.clearcolor = (0.1, 0.1, 0.1, 1)
        root_layout = FloatLayout()
        
        self.card = RoundedCard(
            orientation="vertical", 
            padding=20, 
            spacing=15,
            size_hint=(0.9, 0.85), 
            pos_hint={"center_x": 0.5, "center_y": 0.5}
        )
        
        self._create_title_label()
        self._create_genre_buttons()
        self._create_generate_button()
        self._create_message_label()
        self._create_history_section()
        
        root_layout.add_widget(self.card)
        self.add_widget(root_layout)
    
    def on_enter(self):
        """Executado quando a tela é exibida."""
        app = App.get_running_app()
        self.title_label.text = f"Olá, {app.user_name}! Escolha um gênero para receber uma sugestão."
    
    def _create_title_label(self):
        """Cria o rótulo de título da tela."""
        self.title_label = Label(
            text="", 
            font_size=24, 
            bold=True, 
            color=(0, 1, 0.6, 1), 
            size_hint=(1, 0.2)
        )
        self.card.add_widget(self.title_label)
    
    def _create_genre_buttons(self):
        """Cria os botões de seleção de gênero."""
        self.genre_buttons_layout = BoxLayout(size_hint=(1, 0.15), spacing=10)
        self.genres = list(self.movie_suggester.movies.keys())
        self.toggle_buttons = {}
        
        for genre in self.genres:
            button = ToggleButton(text=genre, group='genres', size_hint=(1, 1))
            self.toggle_buttons[genre] = button
            self.genre_buttons_layout.add_widget(button)
        
        self.card.add_widget(self.genre_buttons_layout)
    
    def _create_generate_button(self):
        """Cria o botão para gerar sugestões."""
        self.generate_button = Button(
            text="GERAR FILME", 
            size_hint=(1, 0.2),
            background_normal='', 
            background_color=(0, 0.8, 0.4, 1),
            font_size=20, 
            color=(0, 0, 0, 1)
        )
        self.generate_button.bind(on_press=self._suggest_movie)
        self.card.add_widget(self.generate_button)
    
    def _create_message_label(self):
        """Cria o rótulo para exibir mensagens."""
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
        self.card.add_widget(self.message_label)
    
    def _create_history_section(self):
        """Cria a seção de histórico de sugestões."""
        self.history_scroll = ScrollView(size_hint=(1, None), height=0)
        self.history_container = BoxLayout(
            orientation='vertical', 
            size_hint_y=None, 
            spacing=10, 
            padding=5
        )
        self.history_container.bind(minimum_height=self.history_container.setter('height'))
        self.history_scroll.add_widget(self.history_container)
        self.card.add_widget(self.history_scroll)
    
    def _adjust_text_wrapping(self, instance, value):
        """Ajusta o quebra-texto do rótulo de mensagem."""
        instance.text_size = instance.size
    
    def _show_popup(self, title, message):
        """Exibe um popup com uma mensagem para o usuário."""
        popup = Popup(title=title, content=Label(text=message), size_hint=(0.8, 0.4))
        popup.open()
    
    def _validate_input(self, name, age_text, selected_genre):
        """Valida os dados de entrada do usuário."""
        if not age_text.isdigit():
            self._show_popup("Erro de Validação", "Digite uma idade válida!")
            return False
        
        age = int(age_text)
        min_age, max_age = self.movie_suggester.get_age_limits(selected_genre)
        
        if age < min_age or age > max_age:
            self._show_popup("Restrição de Idade", 
                           f"Idade deve estar entre {min_age} e {max_age} para {selected_genre}.")
            return False
        
        return True
    
    def _suggest_movie(self, instance):
        """Processa a solicitação de sugestão de filme."""
        app = App.get_running_app()
        name = app.user_name
        age_text = app.user_age
        selected_genre = next((genre for genre, btn in self.toggle_buttons.items() 
                              if btn.state == 'down'), None)
        
        if not self._validate_input(name, age_text, selected_genre):
            return
        
        suggested_movie = self.movie_suggester.suggest_movie(selected_genre)
        if suggested_movie:
            self._display_movie_suggestion(name, selected_genre, suggested_movie)
            self._add_to_history(name, suggested_movie)
    
    def _display_movie_suggestion(self, name, genre, movie):
        """Exibe a sugestão de filme na interface."""
        movie_title, movie_year, _ = movie
        self.message_label.text = (
            f"[b][color=00ff99]Olá, {name}![/color][/b]\n"
            f"Sua sugestão é:\n[color=ff00ff]{movie_title} ({movie_year})[/color]"
        )
    
    def _add_to_history(self, name, movie):
        """Adiciona a sugestão atual ao histórico."""
        movie_title, movie_year, image_filename = movie
        image_path = os.path.join(os.path.dirname(__file__), image_filename)
        
        if os.path.exists(image_path):
            movie_image = Image(
                source=image_path, 
                size_hint=(1, None), 
                height=200
            )
            self.history_container.add_widget(movie_image)
        
        history_label = Label(
            text=f"{name} sugeriu: {movie_title} ({movie_year})",
            color=(1, 1, 1, 1), 
            size_hint_y=None, 
            height=30
        )
        self.history_container.add_widget(history_label)
        
        self._update_history_display()
    
    def _update_history_display(self):
        """Atualiza a exibição do histórico."""
        self.history_scroll.height = min(300, self.history_container.height)
        if self.history_container.children:
            self.history_scroll.scroll_to(self.history_container.children[0])


class MovieSuggestionApp(App):
    """Aplicativo principal com gerenciamento de telas."""
    
    def build(self):
        """Constrói o aplicativo com gerenciador de telas."""
        self.user_name = ""
        self.user_age = ""
        self.screen_manager = ScreenManager()
        
        self.screen_manager.add_widget(WelcomeScreen(name="welcome"))
        self.screen_manager.add_widget(SuggestionScreen(name="suggestion"))
        
        return self.screen_manager


if __name__ == "__main__":
    MovieSuggestionApp().run()
```