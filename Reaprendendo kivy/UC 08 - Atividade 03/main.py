from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class IdadeApp(App):
    def build(self):
        # Layout principal na vertical
        self.layout = BoxLayout(orientation="vertical", padding=20, spacing=15)

        # Título
        self.title_label = Label(
            text="App de Idade e Acesso",
            font_size=28,
            bold=True,
            size_hint=(1, 0.2)
        )
        self.layout.add_widget(self.title_label)

        # Campo Nome
        self.name_input = TextInput(
            hint_text="Digite seu nome",
            multiline=False,
            size_hint=(1, 0.2)
        )
        self.layout.add_widget(self.name_input)

        # Campo Idade
        self.age_input = TextInput(
            hint_text="Digite sua idade",
            multiline=False,
            input_filter="int",  # aceita só números
            size_hint=(1, 0.2)
        )
        self.layout.add_widget(self.age_input)

        # Botão Enviar
        self.button = Button(
            text="Enviar",
            size_hint=(1, 0.2),
            background_color=(0.1, 0.7, 0.3, 1),  # verde
            font_size=20
        )
        self.button.bind(on_press=self.verificar_idade)
        self.layout.add_widget(self.button)

        # Mensagem final
        self.message_label = Label(
            text="",
            font_size=20,
            halign="center",
            valign="middle",
            size_hint=(1, 0.4)
        )
        self.layout.add_widget(self.message_label)

        return self.layout

    def verificar_idade(self, instance):
        nome = self.name_input.text.strip()
        idade_texto = self.age_input.text.strip()

        if not nome or not idade_texto:
            self.message_label.text = "Por favor, preencha todos os campos."
            return

        try:
            idade = int(idade_texto)
        except ValueError:
            self.message_label.text = "Digite uma idade válida (somente números)."
            return

        # Lógica de verificação
        if idade < 18:
            self.message_label.text = f"Olá, {nome}! Você é menor de idade."
        elif idade >= 60:
            self.message_label.text = f"Olá, {nome}! Você é idoso :D."
        else:
            self.message_label.text = f"Olá, {nome}! Você é maior de idade."


# Rodar o app
if __name__ == "__main__":
    IdadeApp().run()
