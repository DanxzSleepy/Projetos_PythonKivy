from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import DictProperty
from kivy.lang import Builder

Builder.load_file("dict_prop.kv")

class UserProfileWidget(BoxLayout):
    user_data = DictProperty({'name': 'João', 'age': 30, 'city': 'São Paulo'})

    def update_age(self):
        self.user_data['age'] += 1

class DictPropApp(App):
    def build(self):
        return UserProfileWidget()

if __name__ == '__main__':
    DictPropApp().run()
