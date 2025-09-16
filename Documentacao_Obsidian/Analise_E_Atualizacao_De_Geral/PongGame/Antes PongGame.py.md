```python
from kivy.app import App

from kivy.uix.widget import Widget

from kivy.properties import (

    NumericProperty, ReferenceListProperty, ObjectProperty

)

from kivy.vector import Vector

from kivy.clock import Clock

from kivy.core.window import Window  # Importação adicionada

from kivy.graphics import Color, Rectangle, Ellipse

  

class PongPaddle(Widget):

    score = NumericProperty(0)

  
  

    def __init__(self, color=(1, 1, 1), **kwargs):  # cor padrão branca

        super(PongPaddle, self).__init__(**kwargs)

        self.color_rgb = color  # salva a cor

        with self.canvas.before:

            self.color_instruction = Color(*self.color_rgb)

            self.rect = Rectangle(pos=self.pos, size=self.size)

  

        # Atualiza quando mover ou redimensionar

        self.bind(pos=self.update_graphics, size=self.update_graphics)

  

    def update_graphics(self, *args):

        self.rect.pos = self.pos

        self.rect.size = self.size

  

    def bounce_ball(self, ball):

        if self.collide_widget(ball):

            vx, vy = ball.velocity

            offset = (ball.center_y - self.center_y) / (self.height / 2)

            bounced = Vector(-1 * vx, vy)

            vel = bounced * 1.1

            ball.velocity = vel.x, vel.y + offset

  

            ball.set_color(self.color_rgb)  # muda a cor da bola

  
  

class PongBall(Widget):

    velocity_x = NumericProperty(0)

    velocity_y = NumericProperty(0)

    velocity = ReferenceListProperty(velocity_x, velocity_y)

  

    def __init__(self, **kwargs):

        super(PongBall, self).__init__(**kwargs)

        with self.canvas.before:

            self.color_instruction = Color(1, 1, 1)  # cor inicial branca

            self.ellipse = Ellipse(pos=self.pos, size=self.size)

  

        self.bind(pos=self.update_graphics, size=self.update_graphics)

  

    def update_graphics(self, *args):

        self.ellipse.pos = self.pos

        self.ellipse.size = self.size

  

    def move(self):

        self.pos = Vector(*self.velocity) + self.pos

  

    def set_color(self, rgb):

        self.color_instruction.rgb = rgb

  
  

class PongGame(Widget):

    ball = ObjectProperty(None)

    player1 = ObjectProperty(None)

    player2 = ObjectProperty(None)

  

    move_p1 = 0  # -1 para cima, 1 para baixo, 0 para parado

    move_p2 = 0

  

    def __init__(self, **kwargs):

        super(PongGame, self).__init__(**kwargs)

        self._keyboard = Window.request_keyboard(self._on_keyboard_closed, self)

        if self._keyboard.widget:

            pass  # caso esteja usando algum TextInput

        self._keyboard.bind(on_key_down=self.on_key_down)

  

    def _on_keyboard_closed(self):

        print('Teclado desconectado')

        self._keyboard.unbind(on_key_down=self.on_key_down)

        self._keyboard = None

  

    def serve_ball(self, vel=(4, 0)):

        self.ball.center = self.center

        self.ball.velocity = vel

  

    def update(self, dt):

        self.ball.move()

  

        # Movimento contínuo dos paddles

        self.player1.center_y += self.move_p1 * 5  # 5 é a velocidade

        self.player2.center_y += self.move_p2 * 5

  

        # bounce off paddles

        self.player1.bounce_ball(self.ball)

        self.player2.bounce_ball(self.ball)

  

        # bounce ball off bottom or top

        if (self.ball.y < self.y) or (self.ball.top > self.top):

            self.ball.velocity_y *= -1

  

        # went off to a side to score point?

        if self.ball.x < self.x:

            self.player2.score += 1

            self.serve_ball(vel=(4, 0))

        if self.ball.right > self.width:

            self.player1.score += 1

            self.serve_ball(vel=(-4, 0))

  

        self.player1.top = min(self.top, self.player1.top)

        self.player1.y = max(self.y, self.player1.y)

        self.player2.top = min(self.top, self.player2.top)

        self.player2.y = max(self.y, self.player2.y)    

  

    def on_key_down(self, keyboard, keycode, text, modifiers):

        print(f"DEBUG tecla: text={text}, keycode={keycode}")

  

        # Movimento do jogador 1 (W/S)

        if text and text.lower() == 'w':

            self.player1.center_y += 20

        elif text and text.lower() == 's':

            self.player1.center_y -= 20

  

        # Movimento do jogador 2 (setas cima/baixo)

        elif keycode[1] == 'up':

            self.player2.center_y += 20

        elif keycode[1] == 'down':

            self.player2.center_y -= 20

  

        # Movimento do jogador 1 (W/S)

        if keycode[1] == 'w':

            self.move_p1 = 1

        elif keycode[1] == 's':

            self.move_p1 = -1

  

        # Movimento do jogador 2 (setas cima/baixo)

        elif keycode[1] == 'up':

            self.move_p2 = 1

        elif keycode[1] == 'down':

            self.move_p2 = -1    

  

        # Aplica os limites

        self.player1.top = min(self.top, self.player1.top)

        self.player1.y = max(self.y, self.player1.y)

        self.player2.top = min(self.top, self.player2.top)

        self.player2.y = max(self.y, self.player2.y)

  

        return True

  

    def on_key_up(self, keyboard, keycode):

        print(f"DEBUG tecla solta: keycode={keycode}")

  

        # Jogador 1

        if keycode[1] in ('w', 's'):

            self.move_p1 = 0

  

        # Jogador 2

        elif keycode[1] in ('up', 'down'):

            self.move_p2 = 0

  

        return True

  

    def on_touch_move(self, touch):

        speed = 10  # Ajuste este valor para mudar a velocidade

        # Jogador 1

        if touch.x < self.width / 3:

            diff = touch.y - self.player1.center_y

            self.player1.center_y += diff * 0.1  # Movimento suavizado

        # Jogador 2

        if touch.x > self.width - self.width / 3:

            diff = touch.y - self.player2.center_y

            self.player2.center_y += diff * 0.1  # Movimento suavizado

        # Aplica os limites

        self.player1.top = min(self.top, self.player1.top)

        self.player1.y = max(self.y, self.player1.y)

        self.player2.top = min(self.top, self.player2.top)

        self.player2.y = max(self.y, self.player2.y)

  
  

class PongApp(App):

    def build(self):

        game = PongGame()

        game.serve_ball()

        Clock.schedule_interval(game.update, 1.0 / 60.0)

        # Define cores dos jogadores

        game.player1.color_rgb = (1, 0, 0)  # Vermelho

        game.player2.color_rgb = (0, 0, 1)  # Azul

  

        # Atualiza os desenhos dos paddles

        game.player1.color_instruction.rgb = game.player1.color_rgb

        game.player2.color_instruction.rgb = game.player2.color_rgb

  

        return game

  

if __name__ == '__main__':

    PongApp().run()
```