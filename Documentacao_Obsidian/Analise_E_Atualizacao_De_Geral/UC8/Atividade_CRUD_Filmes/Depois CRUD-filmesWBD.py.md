```python
import sqlite3
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image


class DatabaseManager:
    """Classe responsável por gerenciar todas as operações do banco de dados."""
    
    DATABASE_NAME = "filmes.db"
    
    @staticmethod
    def create_database():
        """Cria a tabela de filmes se não existir."""
        with sqlite3.connect(DatabaseManager.DATABASE_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS filmes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    titulo TEXT NOT NULL,
                    genero TEXT NOT NULL,
                    ano INTEGER NOT NULL,
                    imagem TEXT
                )
            """)
            conn.commit()
    
    @staticmethod
    def add_movie(title, genre, year, image_path=None):
        """Adiciona um novo filme ao banco de dados."""
        with sqlite3.connect(DatabaseManager.DATABASE_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO filmes (titulo, genero, ano, imagem) VALUES (?, ?, ?, ?)", 
                (title, genre, year, image_path)
            )
            conn.commit()
    
    @staticmethod
    def get_all_movies():
        """Retorna todos os filmes do banco de dados."""
        with sqlite3.connect(DatabaseManager.DATABASE_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM filmes")
            return cursor.fetchall()
    
    @staticmethod
    def get_movie_by_id(movie_id):
        """Retorna um filme específico pelo ID."""
        with sqlite3.connect(DatabaseManager.DATABASE_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM filmes WHERE id=?", (movie_id,))
            return cursor.fetchone()
    
    @staticmethod
    def update_movie(movie_id, title, genre, year, image_path):
        """Atualiza os dados de um filme existente."""
        with sqlite3.connect(DatabaseManager.DATABASE_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE filmes SET titulo=?, genero=?, ano=?, imagem=? WHERE id=?", 
                (title, genre, year, image_path, movie_id)
            )
            conn.commit()
    
    @staticmethod
    def delete_movie(movie_id):
        """Remove um filme do banco de dados."""
        with sqlite3.connect(DatabaseManager.DATABASE_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM filmes WHERE id=?", (movie_id,))
            conn.commit()


class MovieItem(BoxLayout):
    """Widget personalizado para exibir cada filme na lista."""
    
    movie_id = StringProperty()
    title = StringProperty()
    genre = StringProperty()
    year = StringProperty()
    image_path = StringProperty()
    
    def __init__(self, movie_id, title, genre, year, image_path=None, **kwargs):
        super().__init__(**kwargs)
        self.movie_id = str(movie_id)
        self.title = title
        self.genre = genre
        self.year = str(year)
        self.image_path = image_path or ""
        self._setup_ui()
    
    def _setup_ui(self):
        """Configura a interface do item de filme."""
        self.orientation = "horizontal"
        self.size_hint_y = None
        self.height = 100
        self.spacing = 10
        self.padding = 5
        
        # Imagem do filme (se existir)
        if self.image_path:
            movie_image = Image(
                source=self.image_path, 
                size_hint_x=0.3,
                allow_stretch=True
            )
            self.add_widget(movie_image)
        
        # Informações do filme
        info_label = Label(
            text=f"{self.title} ({self.year}) - {self.genre}",
            size_hint_x=0.6,
            text_size=(None, None),
            halign="left",
            valign="middle"
        )
        info_label.bind(texture_size=info_label.setter('size'))
        self.add_widget(info_label)
        
        # Botão Editar
        edit_button = Button(
            text="Editar", 
            size_hint_x=0.1,
            on_release=self._edit_movie
        )
        self.add_widget(edit_button)
        
        # Botão Excluir
        delete_button = Button(
            text="Excluir", 
            size_hint_x=0.1,
            on_release=self._delete_movie
        )
        self.add_widget(delete_button)
    
    def _edit_movie(self, instance):
        """Navega para a tela de edição do filme."""
        app = App.get_running_app()
        edit_screen = app.root.get_screen("edit")
        edit_screen.load_movie_data(self.movie_id)
        app.root.current = "edit"
    
    def _delete_movie(self, instance):
        """Exclui o filme e atualiza a lista."""
        DatabaseManager.delete_movie(int(self.movie_id))
        app = App.get_running_app()
        app.root.get_screen("list").update_movie_list()


class RegistrationScreen(Screen):
    """Tela de cadastro de novos filmes."""
    
    title_input = ObjectProperty(None)
    genre_input = ObjectProperty(None)
    year_input = ObjectProperty(None)
    image_input = ObjectProperty(None)
    
    def save_movie(self):
        """Salva um novo filme no banco de dados."""
        if self._validate_input():
            DatabaseManager.add_movie(
                self.title_input.text.strip(),
                self.genre_input.text.strip(),
                int(self.year_input.text),
                self.image_input.text.strip() or None
            )
            self._clear_fields()
            self._show_popup("Sucesso", "Filme salvo com sucesso!")
        else:
            self._show_popup("Erro", "Preencha todos os campos corretamente!")
    
    def _validate_input(self):
        """Valida os dados de entrada do usuário."""
        return (self.title_input.text.strip() and 
                self.genre_input.text.strip() and 
                self.year_input.text.isdigit())
    
    def _clear_fields(self):
        """Limpa todos os campos de entrada."""
        self.title_input.text = ""
        self.genre_input.text = ""
        self.year_input.text = ""
        self.image_input.text = ""
    
    def _show_popup(self, title, message):
        """Exibe um popup com mensagem para o usuário."""
        popup = Popup(
            title=title, 
            content=Label(text=message),
            size_hint=(0.6, 0.4)
        )
        popup.open()


class ListScreen(Screen):
    """Tela de listagem de filmes cadastrados."""
    
    movie_list = ObjectProperty(None)
    
    def on_pre_enter(self):
        """Executado antes da tela ser exibida."""
        self.update_movie_list()
    
    def update_movie_list(self):
        """Atualiza a lista de filmes exibida."""
        self.movie_list.clear_widgets()
        movies = DatabaseManager.get_all_movies()
        
        for movie in movies:
            movie_item = MovieItem(
                movie_id=movie[0],
                title=movie[1],
                genre=movie[2],
                year=movie[3],
                image_path=movie[4]
            )
            self.movie_list.add_widget(movie_item)


class EditScreen(Screen):
    """Tela de edição de filmes existentes."""
    
    title_input = ObjectProperty(None)
    genre_input = ObjectProperty(None)
    year_input = ObjectProperty(None)
    image_input = ObjectProperty(None)
    
    current_movie_id = None
    
    def load_movie_data(self, movie_id):
        """Carrega os dados do filme para edição."""
        self.current_movie_id = movie_id
        movie = DatabaseManager.get_movie_by_id(int(movie_id))
        
        if movie:
            self.title_input.text = movie[1]
            self.genre_input.text = movie[2]
            self.year_input.text = str(movie[3])
            self.image_input.text = movie[4] if movie[4] else ""
    
    def save_edits(self):
        """Salva as alterações do filme editado."""
        if self._validate_input() and self.current_movie_id:
            DatabaseManager.update_movie(
                int(self.current_movie_id),
                self.title_input.text.strip(),
                self.genre_input.text.strip(),
                int(self.year_input.text),
                self.image_input.text.strip() or None
            )
            self._show_popup("Sucesso", "Filme atualizado com sucesso!")
            self._navigate_to_list()
        else:
            self._show_popup("Erro", "Preencha todos os campos corretamente!")
    
    def _validate_input(self):
        """Valida os dados de entrada do usuário."""
        return (self.title_input.text.strip() and 
                self.genre_input.text.strip() and 
                self.year_input.text.isdigit())
    
    def _navigate_to_list(self):
        """Navega de volta para a tela de listagem."""
        self.manager.current = "list"
    
    def _show_popup(self, title, message):
        """Exibe um popup com mensagem para o usuário."""
        popup = Popup(
            title=title, 
            content=Label(text=message),
            size_hint=(0.6, 0.4)
        )
        popup.open()


class MovieApp(App):
    """Aplicativo principal de gerenciamento de filmes."""
    
    def build(self):
        """Constrói a interface do aplicativo."""
        DatabaseManager.create_database()
        
        screen_manager = ScreenManager()
        screen_manager.add_widget(RegistrationScreen(name="register"))
        screen_manager.add_widget(ListScreen(name="list"))
        screen_manager.add_widget(EditScreen(name="edit"))
        
        return screen_manager


if __name__ == "__main__":
    MovieApp().run()
```