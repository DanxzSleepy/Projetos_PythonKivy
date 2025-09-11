from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

Builder.load_file('login.kv')

class LoginScreen(BoxLayout):
    def login(self):
        email = self.ids.email_input.text.strip()
        password = self.ids.password_input.text.strip()

        if not email or not password:
            self.ids.message_label.text = "[color=ff0000]Preencha todos os campos![/color]"
            self.ids.message_label.markup = True
            return

        if email == "admin@exemplo.com" and password == "12345":
            self.ids.message_label.text = "[color=00ff00]Login bem-sucedido![/color]"
            self.ids.message_label.markup = True
        else:
            self.ids.message_label.text = "[color=ff0000]E-mail ou senha incorretos.[/color]"
            self.ids.message_label.markup = True


class LoginApp(App):
    def build(self):
        return LoginScreen()


if __name__ == '__main__':
    LoginApp().run()
