# Objetivo: Armazenar dados estruturados (nome, idade, cidade) e atualizar dinamicamente.

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import DictProperty

class UserProfileWidget(BoxLayout):
    user_data = DictProperty({'name': 'Jonas', 'age': 30, 'city': 'São Paulo'})

    def update_age(self):
        self.user_data['age'] += 1
        self.user_data = self.user_data  # força atualização

class DictPropApp(App):
    def build(self):
        return UserProfileWidget()

if __name__ == '__main__':
    DictPropApp().run()
