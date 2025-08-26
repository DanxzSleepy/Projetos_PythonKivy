from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

class IdadeApp(App):
    def build(self):
        # Cor de fundo (cinza claro)
        Window.clearcolor = (0.95, 0.95, 0.95, 1)

        # Layout principal
        self.layout = BoxLayout(orientation="vertical", padding=20, spacing=15)

        # Título
        self.title_label = Label(
            text="App de Idade e Acesso",
            font_size=28,
            bold=True,
            color=(0.2, 0.2, 0.6, 1),  # azul escuro
            size_hint=(1, 0.2)
        )
        self.layout.add_widget(self.title_label)

        # Campo Nome
        self.name_input = TextInput(
            hint_text="Digite seu nome",
            multiline=False,
            size_hint=(1, 0.15),
            background_color=(1, 1, 1, 1),
            foreground_color=(0, 0, 0, 1)
        )
        self.layout.add_widget(self.name_input)

        # Campo Idade
        self.age_input = TextInput(
            hint_text="Digite sua idade",
            multiline=False,
            input_filter="int",
            size_hint=(1, 0.15),
            background_color=(1, 1, 1, 1),
            foreground_color=(0, 0, 0, 1)
        )
        self.layout.add_widget(self.age_input)

        # Botão Enviar
        self.button = Button(
            text="Enviar",
            size_hint=(1, 0.2),
            background_normal='',  # garante a cor
            background_color=(0.1, 0.7, 0.3, 1),  # verde
            font_size=20,
            color=(1, 1, 1, 1)
        )
        self.button.bind(on_press=self.verificar_idade)
        self.layout.add_widget(self.button)

        # Mensagem final
        self.message_label = Label(
            text="",
            font_size=20,
            halign="center",
            valign="middle",
            size_hint=(1, 0.3),
            color=(0, 0, 0, 1)  # padrão preto
        )
        self.message_label.bind(size=self.ajustar_texto)
        self.layout.add_widget(self.message_label)

        return self.layout

    def ajustar_texto(self, instance, value):
        # Faz o texto centralizar de verdade
        instance.text_size = instance.size

    def verificar_idade(self, instance):
        nome = self.name_input.text.strip()
        idade_texto = self.age_input.text.strip()

        if not nome or not idade_texto:
            self.message_label.text = "Por favor, preencha todos os campos."
            self.message_label.color = (1, 0, 0, 1)  # vermelho
            return

        try:
            idade = int(idade_texto)
        except ValueError:
            self.message_label.text = "Digite uma idade válida (somente números)."
            self.message_label.color = (1, 0, 0, 1)  # vermelho
            return

        # Lógica de verificação
        if idade < 18:
            self.message_label.text = f"Olá, {nome}! Você é menor de idade."
            self.message_label.color = (0.9, 0.6, 0.1, 1)  # laranja
        elif idade >= 60:
            self.message_label.text = f"Olá, {nome}! Você é um idoso :D."
            self.message_label.color = (0.1, 0.5, 0.9, 1)  # azul
        else:
            self.message_label.text = f"Olá, {nome}! Você é maior de idade."
            self.message_label.color = (0.1, 0.7, 0.3, 1)  # verde


if __name__ == "__main__":
    IdadeApp().run()

# Pontos a Melhorados

# Estética do app
#   Falta padronização de cores (fundo padrão cinza do Kivy).
#   Poderia adicionar Window.clearcolor para deixar o fundo mais agradável.
#   Labels e botão poderiam ter cores e fontes mais destacadas.

# Centralização da mensagem final
# Ele usou halign e valign, mas esqueceu de vincular text_size. Sem isso, o texto não centraliza de verdade.

# Feedback visual do botão
#   Só tem background_color, mas faltou background_normal='' para garantir que a cor apareça corretamente em todas as plataformas.

# Mensagem de erro
#   As mensagens poderiam ter cores diferentes (ex: vermelho para erro, verde/azul para sucesso), tornando mais claro para o usuário.