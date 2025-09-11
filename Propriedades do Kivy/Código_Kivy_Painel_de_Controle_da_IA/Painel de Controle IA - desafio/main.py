import json
import os
from datetime import datetime
from random import randint
from threading import Thread

from kivy.app import App
from kivy.clock import Clock, mainthread
from kivy.core.audio import SoundLoader
from kivy.properties import BooleanProperty, StringProperty, NumericProperty, ListProperty
from kivy.uix.boxlayout import BoxLayout


ESTADO_PATH = "estado_ia.json"


class PainelIA(BoxLayout):
    ia_ativa = BooleanProperty(False)
    status_texto = StringProperty("IA Desativada")
    comando_resposta = StringProperty("")
    nivel_ameaca = NumericProperty(0)
    log_eventos = ListProperty([])

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.som_alerta = SoundLoader.load("alarme.wav")  # coloque um arquivo .wav na pasta
        self.carregar_estado()

    def log(self, mensagem):
        timestamp = datetime.now().strftime("[%H:%M:%S]")
        entrada = f"{timestamp} {mensagem}"
        self.log_eventos.append(entrada)

        if len(self.log_eventos) > 100:
            self.log_eventos = self.log_eventos[-100:]

    def alternar_ia(self):
        self.ia_ativa = not self.ia_ativa
        self.status_texto = "IA Ativada" if self.ia_ativa else "IA Desativada"
        self.log("IA ligada." if self.ia_ativa else "IA desligada.")
        self.nivel_ameaca = randint(10, 30) if self.ia_ativa else 0

        if self.ia_ativa:
            Clock.schedule_interval(self.atualizar_ameaca, 1)
            Thread(target=self.simular_tarefa_background, daemon=True).start()
        else:
            Clock.unschedule(self.atualizar_ameaca)

        self.salvar_estado()

    def atualizar_ameaca(self, dt):
        if not self.ia_ativa:
            return

        incremento = randint(0, 5)
        self.nivel_ameaca = min(100, self.nivel_ameaca + incremento)

        if self.nivel_ameaca >= 80:
            if self.som_alerta:
                self.som_alerta.play()
            self.status_texto = "⚠️ Nível Crítico de Ameaça!"
        if self.nivel_ameaca >= 100:
            self.status_texto = "🛑 Ameaça Máxima! IA Instável!"
            self.log("Sistema atingiu o nível máximo de ameaça!")
            Clock.unschedule(self.atualizar_ameaca)

        self.salvar_estado()

    def enviar_comando(self):
        if not self.ia_ativa:
            resposta = "IA está desligada. Ligue-a para enviar comandos."
        else:
            comando = self.ids.campo_comando.text.strip().lower()

            respostas = {
                "injetar_virus": "IA: Tentativa de injeção bloqueada.",
                "desligar_sistemas": "IA: Subsistemas desligados com sucesso.",
                "acessar_dados": "IA: Dados confidenciais acessados.",
                "diagnostico": "IA: Sondas de diagnóstico lançadas.",
            }

            if comando in respostas:
                resposta = respostas[comando]
                self.nivel_ameaca += randint(5, 15)
                self.nivel_ameaca = min(self.nivel_ameaca, 100)
            elif comando == "":
                resposta = "Digite um comando válido."
            else:
                resposta = f"IA: Comando '{comando}' não reconhecido."

        self.comando_resposta = resposta
        self.ids.campo_comando.text = ""
        self.log(f"Comando: {resposta}")
        self.salvar_estado()

    def simular_tarefa_background(self):
        import time
        for _ in range(5):
            if not self.ia_ativa:
                return
            time.sleep(randint(2, 5))
            self.executar_log_em_thread("IA: Analisando padrões em segundo plano...")

    @mainthread
    def executar_log_em_thread(self, texto):
        self.log(texto)

    def salvar_estado(self):
        estado = {
            "ia_ativa": self.ia_ativa,
            "nivel_ameaca": self.nivel_ameaca,
            "log_eventos": self.log_eventos[-50:],
        }
        with open(ESTADO_PATH, "w") as f:
            json.dump(estado, f)

    def carregar_estado(self):
        if os.path.exists(ESTADO_PATH):
            with open(ESTADO_PATH, "r") as f:
                estado = json.load(f)
                self.ia_ativa = estado.get("ia_ativa", False)
                self.nivel_ameaca = estado.get("nivel_ameaca", 0)
                self.log_eventos = estado.get("log_eventos", [])
                self.status_texto = "IA Ativada" if self.ia_ativa else "IA Desativada"
                if self.ia_ativa:
                    Clock.schedule_once(lambda dt: self.alternar_ia(), 0.5)


class PainelIAApp(App):
    def build(self):
        return PainelIA()
