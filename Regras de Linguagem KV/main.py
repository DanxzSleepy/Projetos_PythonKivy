from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty

class RootWidget(BoxLayout):
    # Propriedade reativa ligada à Label na interface
    greeting = StringProperty("Olá! Digite seu nome acima.")

    def update_greeting(self):
        # Lê o texto do TextInput via id e atualiza a greeting
        nome = self.ids.input_name.text.strip()
        if nome:
            self.greeting = f"Olá, {nome}!"
        else:
            self.greeting = "Olá! Digite seu nome acima."

class GreetingApp(App):
    def build(self):
        return RootWidget()

if __name__ == "__main__":
    GreetingApp().run()


