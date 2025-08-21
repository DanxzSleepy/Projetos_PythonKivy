from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

Builder.load_file('login.kv')

class LoginScreen(BoxLayout):
    def login(self):
        email = self.ids.email_input.text
        password = self.ids.password_input.text

        if email == "admin@exemplo.com" and password == "12345":
            print("✅ Login bem-sucedido!")
        else:
            print("❌ Login falhou. E-mail ou senha incorretos.")

class LoginApp(App):
    def build(self):
        self.title = "Login - Estilo 2000"
        return LoginScreen()

if __name__ == '__main__':
    LoginApp().run()
