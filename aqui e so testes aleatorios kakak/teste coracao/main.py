import random
import math
import turtle
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock


# -------------------------------
# PARTE DO TURTLE - CORAÇÕES
# -------------------------------
def desenhar_coracoes():
    screen = turtle.Screen()
    screen.bgcolor("black")
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()

    def coracao(n):
        x = 16 * math.sin(n) ** 3
        y = 13 * math.cos(n) - 5 * math.cos(2 * n) - 2 * math.cos(3 * n) - math.cos(4 * n)
        return x, y

    # vários corações espalhados
    for j in range(5):  # quantidade de corações
        t.penup()
        offset_x = random.randint(-200, 200)
        offset_y = random.randint(-200, 200)
        t.goto(offset_x, offset_y)
        t.pendown()
        t.color(random.choice(["red", "pink", "purple"]))
        for i in range(1, 10):  # camadas de cada coração
            t.penup()
            t.goto(offset_x, offset_y)
            t.pendown()
            for n in range(0, 628, 15):
                x, y = coracao(n / 100)
                t.goto(x * i + offset_x, y * i + offset_y)

    # Escreve a mensagem no meio
    t.penup()
    t.goto(0, -50)
    t.color("white")
    t.write("EU também gosto de você 🌹\nI love you too 🌹",
            align="center", font=("Arial", 18, "bold"))

    turtle.done()


# -------------------------------
# PARTE DO KIVY
# -------------------------------
class LoveApp(App):
    def build(self):
        layout = FloatLayout()

        self.label = Label(text="", #Você gosta de mim? 💖
                           font_size=30,
                           pos_hint={"center_x": 0.5, "center_y": 0.8})
        layout.add_widget(self.label)

        self.btn_sim = Button(text="Sim",
                              size_hint=(0.2, 0.1),
                              pos_hint={"center_x": 0.3, "center_y": 0.5})
        self.btn_sim.bind(on_press=self.on_sim)
        layout.add_widget(self.btn_sim)

        self.btn_nao = Button(text="Não",
                              size_hint=(0.2, 0.1),
                              pos_hint={"center_x": 0.7, "center_y": 0.5})
        self.btn_nao.bind(on_press=self.on_nao)
        layout.add_widget(self.btn_nao)

        return layout

    def on_sim(self, instance):
        # chama o turtle
        desenhar_coracoes()

    def on_nao(self, instance):
        # Teleporta e diminui o botão "Não"
        new_x = random.random()
        new_y = random.random()
        instance.pos_hint = {"center_x": new_x, "center_y": new_y}

        # Diminui o botão aos poucos
        if instance.size_hint[0] > 0.05:
            instance.size_hint = (instance.size_hint[0] * 0.8, instance.size_hint[1] * 0.8)
        else:
            instance.opacity = 0  # desaparece


if __name__ == "__main__":
    LoveApp().run()
