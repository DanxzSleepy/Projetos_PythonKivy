```python
import requests
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


class JokeApp(App):
    """Aplicativo que consome API de piadas e exibe para o usuário."""
    
    def build(self):
        """Constrói a interface gráfica do aplicativo."""
        self._setup_ui()
        return self.layout
    
    def _setup_ui(self):
        """Configura todos os componentes da interface do usuário."""
        self.layout = BoxLayout(orientation="vertical", padding=20, spacing=20)
        self._create_joke_label()
        self._create_joke_button()
    
    def _create_joke_label(self):
        """Cria o rótulo para exibir as piadas."""
        self.joke_label = Label(
            text="Clique no botão para ver uma piada!",
            halign="center",
            valign="middle",
            font_size=20
        )
        self.joke_label.bind(size=self._adjust_text_alignment)
        self.layout.add_widget(self.joke_label)
    
    def _create_joke_button(self):
        """Cria o botão para carregar novas piadas."""
        self.joke_button = Button(
            text="Nova Piada",
            size_hint=(1, 0.2),
            font_size=18
        )
        self.joke_button.bind(on_press=self._fetch_joke)
        self.layout.add_widget(self.joke_button)
    
    def _adjust_text_alignment(self, instance, value):
        """Ajusta o alinhamento do texto quando o tamanho do rótulo muda."""
        instance.text_size = instance.size
    
    def _fetch_joke(self, instance):
        """Busca uma nova piada da API e atualiza a interface."""
        try:
            joke_data = self._get_joke_from_api()
            if joke_data:
                self._display_joke(joke_data)
            else:
                self._display_error("Erro ao carregar piada")
        except requests.exceptions.Timeout:
            self._display_error("Tempo limite excedido. Verifique sua conexão.")
        except requests.exceptions.ConnectionError:
            self._display_error("Erro de conexão. Verifique sua internet.")
        except Exception as error:
            self._display_error(f"Erro inesperado: {error}")
    
    def _get_joke_from_api(self):
        """Faz requisição à API de piadas e retorna os dados."""
        api_url = "https://official-joke-api.appspot.com/random_joke"
        response = requests.get(api_url, timeout=10)
        
        if response.status_code == 200:
            return response.json()
        return None
    
    def _display_joke(self, joke_data):
        """Exibe a piada no rótulo formatada adequadamente."""
        setup = joke_data.get("setup", "")
        punchline = joke_data.get("punchline", "")
        self.joke_label.text = f"{setup}\n\n{punchline}"
    
    def _display_error(self, error_message):
        """Exibe mensagem de erro no rótulo."""
        self.joke_label.text = error_message


if __name__ == "__main__":
    JokeApp().run()
```