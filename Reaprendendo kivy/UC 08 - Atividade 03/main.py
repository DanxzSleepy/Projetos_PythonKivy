from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.image import Image

# Definindo uma paleta de cores
class Colors:
    BACKGROUND = (0.95, 0.95, 0.95, 1)
    TITLE_COLOR = (0.2, 0.2, 0.6, 1)  # azul escuro
    BUTTON_COLOR = (0.1, 0.7, 0.3, 1)  # verde
    ERROR_COLOR = (1, 0, 0, 1)  # vermelho
    WARNING_COLOR = (0.9, 0.6, 0.1, 1)  # laranja
    INFO_COLOR = (0.1, 0.5, 0.9, 1)  # azul
    SUCCESS_COLOR = (0.1, 0.7, 0.3, 1)  # verde

class AgeForm(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", padding=20, spacing=15, **kwargs)

        # Título
        self.title_label = Label(
            text="App de Idade e Acesso",
            font_size=28,
            bold=True,
            color=Colors.TITLE_COLOR,
            size_hint=(1, 0.2)
        )
        self.add_widget(self.title_label)

        # Campo Nome
        self.name_input = TextInput(
            hint_text="Digite seu nome",
            multiline=False,
            size_hint=(1, 0.15),
            background_color=(1, 1, 1, 1),
            foreground_color=(0, 0, 0, 1)
        )
        self.add_widget(self.name_input)

        # Campo Idade
        self.age_input = TextInput(
            hint_text="Digite sua idade",
            multiline=False,
            input_filter="int",
            size_hint=(1, 0.15),
            background_color=(1, 1, 1, 1),
            foreground_color=(0, 0, 0, 1)
        )
        self.age_input.bind(on_text_validate=self.validate_input)
        self.add_widget(self.age_input)

        # Botão Enviar
        self.button = Button(
            text="Enviar",
            size_hint=(1, 0.2),
            background_normal='',
            background_color=Colors.BUTTON_COLOR,
            font_size=20,
            color=(1, 1, 1, 1)
        )
        self.button.bind(on_press=self.verify_age)
        self.add_widget(self.button)

        # Mensagem final
        self.message_label = Label(
            text="",
            font_size=20,
            halign="center",
            valign="middle",
            size_hint=(1, 0.3),
            color=(0, 0, 0, 1)
        )
        self.message_label.bind(size=self.adjust_text)
        self.add_widget(self.message_label)

        # Ícone de feedback
        self.feedback_icon = Image(size_hint=(None, None), size=(50, 50))
        self.add_widget(self.feedback_icon)

    def adjust_text(self, instance, value):
        instance.text_size = instance.size

    def validate_input(self, instance):
        if not self.name_input.text.strip():
            self.update_message("Por favor, preencha seu nome.", Colors.ERROR_COLOR, "error.png")
        elif not self.age_input.text.strip():
            self.update_message("Por favor, preencha sua idade.", Colors.ERROR_COLOR, "error.png")
        else:
            self.update_message("", (0, 0, 0, 1), "")

    def update_message(self, message, color, icon_path):
        self.message_label.text = message
        self.message_label.color = color
        self.feedback_icon.source = icon_path
        self.feedback_icon.opacity = 1 if icon_path else 0  # Mostra ou esconde o ícone

    def verify_age(self, instance):
        nome = self.name_input.text.strip()
        idade_texto = self.age_input.text.strip()

        if not nome or not idade_texto:
            self.update_message("Por favor, preencha todos os campos.", Colors.ERROR_COLOR, "error.png")
            return

        try:
            idade = int(idade_texto)
        except ValueError:
            self.update_message("Digite uma idade válida (somente números).", Colors.ERROR_COLOR, "error.png")
            return

        # Lógica de verificação (a foto eu coloco em outro dia slk kakakakakakakak)
        if idade < 13:
            self.update_message(f"Olá, {nome}! Você é uma criança.", Colors.WARNING_COLOR, "warning.png")
        elif idade < 18:
            self.update_message(f"Olá, {nome}! Você é um adolescente.", Colors.WARNING_COLOR, "warning.png")
        elif idade < 30:
            self.update_message(f"Olá, {nome}! Você é um jovem adulto.", Colors.SUCCESS_COLOR, "success.png")
        elif idade < 60:
            self.update_message(f"Olá, {nome}! Você é um adulto.", Colors.SUCCESS_COLOR, "success.png")
        else:
            self.update_message(f"Olá, {nome}! Você é um idoso :D.", Colors.INFO_COLOR, "info.png")

class IdadeApp(App):
    def build(self):
        Window.clearcolor = Colors.BACKGROUND
        return AgeForm()

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

# Pontos melhardos novamente:

# Padronização de estilo
# As cores e tamanhos foram definidos, mas ainda não existe uma paleta consistente para todo o app. Poderia pensar em um tema único (mesma família de cores, harmonia entre labels, botão e fundo).

# Organização da lógica
# A lógica de verificação da idade está toda em um único método. Separar as validações (ex: campos vazios, valores inválidos, faixa etária) em funções auxiliares deixaria o código mais limpo.

# Faixas etárias adicionais
# Ele já adicionou a condição de “idoso”, mas poderia enriquecer ainda mais criando outras categorias (adolescente, jovem adulto, etc.).

# Feedback de entrada
# Atualmente, só há feedback depois de clicar em “Enviar”. Seria interessante melhorar a experiência do usuário, por exemplo, destacando o campo vazio ou inválido já na digitação.

# Reaproveitamento de código
# As mudanças de cor e mensagem se repetem em vários pontos. Criar uma função auxiliar que atualize a mensagem + cor evitaria repetição.

# Escalabilidade
# Hoje, tudo está dentro da classe principal. Pensar em organizar melhor (por exemplo, criar um widget separado para o formulário) ajudaria caso o app cresça no futuro.

# Experiência do usuário
# Melhorar mensagens, cores e feedback visual pode tornar o app mais intuitivo e amigável, especialmente para usuários jovens.

# Mensagens de alerta e sucesso
# Usar cores distintas para sucesso, alerta e erro ajuda o usuário a entender rapidamente o resultado da ação.
