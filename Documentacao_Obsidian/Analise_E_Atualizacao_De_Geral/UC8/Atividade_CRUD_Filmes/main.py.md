```python
import sqlite3

from kivy.app import App

from kivy.uix.screenmanager import ScreenManager, Screen

from kivy.properties import ObjectProperty

from kivy.uix.popup import Popup

from kivy.uix.label import Label

  

# ---------- BANCO DE DADOS ----------

def criar_banco():

    conn = sqlite3.connect("filmes.db")

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

    conn.close()

  

def adicionar_filme(titulo, genero, ano, imagem=None):

    conn = sqlite3.connect("filmes.db")

    cursor = conn.cursor()

    cursor.execute("INSERT INTO filmes (titulo, genero, ano, imagem) VALUES (?, ?, ?, ?)",

                   (titulo, genero, ano, imagem))

    conn.commit()

    conn.close()

  

def listar_filmes():

    conn = sqlite3.connect("filmes.db")

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM filmes")

    filmes = cursor.fetchall()

    conn.close()

    return filmes

  

def editar_filme(filme_id, titulo, genero, ano, imagem):

    conn = sqlite3.connect("filmes.db")

    cursor = conn.cursor()

    cursor.execute("UPDATE filmes SET titulo=?, genero=?, ano=?, imagem=? WHERE id=?",

                   (titulo, genero, ano, imagem, filme_id))

    conn.commit()

    conn.close()

  

def deletar_filme(filme_id):

    conn = sqlite3.connect("filmes.db")

    cursor = conn.cursor()

    cursor.execute("DELETE FROM filmes WHERE id=?", (filme_id,))

    conn.commit()

    conn.close()

  
  

# ---------- TELAS ----------

class CadastroScreen(Screen):

    titulo = ObjectProperty(None)

    genero = ObjectProperty(None)

    ano = ObjectProperty(None)

    imagem = ObjectProperty(None)

  

    def salvar_filme(self):

        if self.titulo.text and self.genero.text and self.ano.text.isdigit():

            adicionar_filme(self.titulo.text, self.genero.text, int(self.ano.text), self.imagem.text or None)

            self.titulo.text = ""

            self.genero.text = ""

            self.ano.text = ""

            self.imagem.text or None

            popup = Popup(title="Sucesso", content=Label(text="Filme salvo com sucesso!"),

                          size_hint=(0.6, 0.4))

            popup.open()

        else:

            popup = Popup(title="Erro", content=Label(text="Preencha todos os campos corretamente!"),

                          size_hint=(0.6, 0.4))

            popup.open()

  
  

class ListagemScreen(Screen):

    lista = ObjectProperty(None)

  

    def on_pre_enter(self):

        self.atualizar_lista()

  

    def atualizar_lista(self):

        self.lista.clear_widgets()

        for filme in listar_filmes():

            item = FilmeItem(filme_id=filme[0], titulo=filme[1], genero=filme[2], ano=str(filme[3]), imagem=filme[4])

            self.lista.add_widget(item)

  
  

class EdicaoScreen(Screen):

    titulo = ObjectProperty(None)

    genero = ObjectProperty(None)

    ano = ObjectProperty(None)

    imagem = ObjectProperty(None)

    filme_id = None

  

    def carregar_dados(self, filme_id, titulo, genero, ano, imagem):

        self.filme_id = filme_id

        self.titulo.text = titulo

        self.genero.text = genero

        self.ano.text = ano

        self.imagem.text = imagem if imagem else ""

  

    def salvar_edicao(self):

        if self.filme_id:

            editar_filme(

            self.filme_id,

            self.titulo.text,

            self.genero.text,

            int(self.ano.text),

            self.imagem.text or None  # Aqui você passa a imagem ou None se estiver vazio

        )

        self.manager.current = "listagem"

  
  

# ---------- WIDGET PERSONALIZADO ----------

from kivy.uix.boxlayout import BoxLayout

from kivy.uix.button import Button

from kivy.uix.image import Image

from kivy.uix.label import Label

  
  

class FilmeItem(BoxLayout):

    def __init__(self, filme_id, titulo, genero, ano, imagem=None, **kwargs):

        super().__init__(**kwargs)

        self.orientation = "horizontal"

        self.size_hint_y = None

        self.height = 100

  

        if imagem:

            self.add_widget(Image(source=imagem, size_hint_x=0.3))

  

        self.filme_id = filme_id

        self.add_widget(Label(text=f"{titulo} ({ano}) - {genero}"))

  

        btn_edit = Button(text="Editar", size_hint_x=0.2)

        btn_edit.bind(on_release=self.editar)

        self.add_widget(btn_edit)

  

        btn_del = Button(text="Excluir", size_hint_x=0.2)

        btn_del.bind(on_release=self.excluir)

        self.add_widget(btn_del)

  

    def editar(self, *args):

        app = App.get_running_app()

        edicao_screen = app.root.get_screen("edicao")

  

        # Busca o filme pelo ID diretamente

        conn = sqlite3.connect("filmes.db")

        cursor = conn.cursor()

        cursor.execute("SELECT * FROM filmes WHERE id=?", (self.filme_id,))

        filme = cursor.fetchone()

        conn.close()

  

        if filme:

            # filme = (id, titulo, genero, ano, imagem)

            edicao_screen.carregar_dados(filme[0], filme[1], filme[2], str(filme[3]), filme[4] if len(filme) > 4 else "")

            app.root.current = "edicao"

  

    def excluir(self, *args):

        deletar_filme(self.filme_id)

        app = App.get_running_app()

        app.root.get_screen("listagem").atualizar_lista()

  
  

# ---------- APP ---------

class FilmeApp(App):

    def build(self):

        criar_banco()

        sm = ScreenManager()

        sm.add_widget(CadastroScreen(name="cadastro"))

        sm.add_widget(ListagemScreen(name="listagem"))

        sm.add_widget(EdicaoScreen(name="edicao"))

        return sm

  

if __name__ == "__main__":

    FilmeApp().run()
```