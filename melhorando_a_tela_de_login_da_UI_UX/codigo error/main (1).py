# Importa a classe principal da aplicação Kivy. Todo app Kivy precisa desta classe.
from kivy.app import App

# Importa o BoxLayout, um tipo de layout que organiza os widgets (botões, textos) em uma caixa
# (vertical ou horizontal). É o mais comum para layouts simples.
from kivy.uix.boxlayout import BoxLayout

# A seguir, importamos os widgets que usaremos na nossa tela de login.
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

# O Builder é usado para carregar e interpretar o arquivo de marcação KV (.kv).
from kivy.lang import Builder

# Carrega o arquivo de marcação 'login.kv'.
# O Kivy irá procurar este arquivo e usar suas regras para construir a interface.
Builder.load_file('login.kv')

# Define a classe 'LoginScreen'. Ela herda de BoxLayout, o que significa que
# ela é um layout que pode conter outros widgets.
# A estrutura visual desta tela será definida no arquivo login.kv.
class LoginScreen(BoxLayout):
    # O método 'login' será chamado quando o usuário clicar no botão 'Entrar'.
    # A lógica de autenticação é implementada aqui.
    def login(self):
        # Acessa o texto digitado no campo de e-mail usando seu 'id' definido no arquivo KV.
        # self.ids.email_input refere-se ao TextInput com id: email_input.
        email = self.ids.email_input.text
        
        # Acessa o texto digitado no campo de senha, também usando seu 'id'.
        password = self.ids.password_input.text

        # Condição de exemplo para verificar se o e-mail e a senha estão corretos.
        # Em uma aplicação real, você faria uma validação mais segura.
        if email == "admin@exemplo.com" and password == "12345":
            # Se a condição for verdadeira, imprime uma mensagem de sucesso no console.
            print("Login bem-sucedido!")
        else:
            # Caso contrário, informa que o login falhou.
            print("Login falhou. E-mail ou senha incorretos.")

# Define a classe principal da aplicação, que herda de App.
# Toda aplicação Kivy deve ter uma classe principal que herda de App.
class LoginApp(App):
    # O método 'build' é o ponto de entrada da aplicação.
    # Ele é chamado automaticamente pelo Kivy quando a aplicação inicia.
    def build(self):
        # Retorna a instância da nossa tela de login, que será exibida como a janela principal.
        return LoginScreen()

# Esta é a parte que executa a aplicação.
# A condição '__name__ == '__main__' garante que o código só seja executado
# se o arquivo for rodado diretamente.
if __name__ == '__main__':
    # Cria uma instância de LoginApp e a executa.
    LoginApp().run()