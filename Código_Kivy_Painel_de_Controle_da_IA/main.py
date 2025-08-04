from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import BooleanProperty, StringProperty, NumericProperty
from kivy.clock import Clock
from random import randint


class PainelIA(BoxLayout):
    ia_ativa = BooleanProperty(False)
    status_texto = StringProperty("IA Desativada")
    comando_resposta = StringProperty("")
    nivel_ameaca = NumericProperty(0)

    def alternar_ia(self):
        self.ia_ativa = not self.ia_ativa
        self.status_texto = "IA Ativada" if self.ia_ativa else "IA Desativada"
        self.nivel_ameaca = 0 if not self.ia_ativa else randint(10, 30)

        if self.ia_ativa:
            Clock.schedule_interval(self.atualizar_ameaca, 1)
        else:
            Clock.unschedule(self.atualizar_ameaca)

    def atualizar_ameaca(self, dt):
        if not self.ia_ativa:
            return

        incremento = randint(0, 5)
        self.nivel_ameaca = min(100, self.nivel_ameaca + incremento)

        if self.nivel_ameaca >= 100:
            self.status_texto = "🛑 Ameaça Máxima! IA Instável!"
            Clock.unschedule(self.atualizar_ameaca)

    def enviar_comando(self):
        if not self.ia_ativa:
            self.comando_resposta = "IA está desligada. Ligue-a para enviar comandos."
            return

        comando = self.ids.campo_comando.text.strip().lower()
        if comando == "":
            self.comando_resposta = "Digite um comando válido."
        else:
            self.comando_resposta = f"Comando '{comando}' executado."
        self.ids.campo_comando.text = ""


class PainelIAApp(App):
    def build(self):
        return PainelIA()


if __name__ == '__main__':
    PainelIAApp().run()
