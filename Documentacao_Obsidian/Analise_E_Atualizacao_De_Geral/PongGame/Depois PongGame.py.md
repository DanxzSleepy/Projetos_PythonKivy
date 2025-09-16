```python
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle, Ellipse

class PongPaddle(Widget):
    """Raquete do jogador com pontuação e cor personalizada."""
    score = NumericProperty(0)

    def __init__(self, color=(1, 1, 1), **kwargs):
        super(PongPaddle, self).__init__(**kwargs)
        self.color_rgb = color  # Armazena a cor RGB da raquete
        
        # Configuração gráfica da raquete
        with self.canvas.before:
            self.color_instruction = Color(*self.color_rgb)
            self.rect = Rectangle(pos=self.pos, size=self.size)

        # Atualiza gráficos quando a raquete se move ou redimensiona
        self.bind(pos=self.update_graphics, size=self.update_graphics)

    def update_graphics(self, *args):
        """Atualiza a posição e tamanho do gráfico da raquete."""
        self.rect.pos = self.pos
        self.rect.size = self.size

    def bounce_ball(self, ball):
        """Faz a bola quicar na raquete com mudança de direção e cor."""
        if self.collide_widget(ball):
            vx, vy = ball.velocity
            offset = (ball.center_y - self.center_y) / (self.height / 2)
            bounced = Vector(-1 * vx, vy)
            vel = bounced * 1.1  # Aumenta ligeiramente a velocidade
            ball.velocity = vel.x, vel.y + offset
            ball.set_color(self.color_rgb)  # Muda a cor da bola para a cor da raquete


class PongBall(Widget):
    """Bola do jogo com propriedades de movimento e cor."""
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def __init__(self, **kwargs):
        super(PongBall, self).__init__(**kwargs)
        
        # Configuração gráfica da bola (cor inicial branca)
        with self.canvas.before:
            self.color_instruction = Color(1, 1, 1)
            self.ellipse = Ellipse(pos=self.pos, size=self.size)

        self.bind(pos=self.update_graphics, size=self.update_graphics)

    def update_graphics(self, *args):
        """Atualiza a posição e tamanho do gráfico da bola."""
        self.ellipse.pos = self.pos
        self.ellipse.size = self.size

    def move(self):
        """Move a bola de acordo com sua velocidade."""
        self.pos = Vector(*self.velocity) + self.pos

    def set_color(self, rgb):
        """Altera a cor da bola."""
        self.color_instruction.rgb = rgb


class PongGame(Widget):
    """Jogo principal que gerencia a lógica do Pong."""
    ball = ObjectProperty(None)
    player1 = ObjectProperty(None)
    player2 = ObjectProperty(None)

    # Controles de movimento contínuo (-1: baixo, 0: parado, 1: cima)
    move_p1 = 0
    move_p2 = 0

    def __init__(self, **kwargs):
        super(PongGame, self).__init__(**kwargs)
        self._setup_keyboard_controls()

    def _setup_keyboard_controls(self):
        """Configura os controles de teclado."""
        self._keyboard = Window.request_keyboard(self._on_keyboard_closed, self)
        self._keyboard.bind(on_key_down=self.on_key_down, on_key_up=self.on_key_up)

    def _on_keyboard_closed(self):
        """Limpa os bindings do teclado quando desconectado."""
        self._keyboard.unbind(on_key_down=self.on_key_down, on_key_up=self.on_key_up)
        self._keyboard = None

    def serve_ball(self, vel=(4, 0)):
        """Posiciona a bola no centro e define sua velocidade inicial."""
        self.ball.center = self.center
        self.ball.velocity = vel

    def update(self, dt):
        """Atualiza o estado do jogo a cada frame."""
        # Movimento da bola
        self.ball.move()

        # Movimento contínuo das raquetes
        paddle_speed = 5
        self.player1.center_y += self.move_p1 * paddle_speed
        self.player2.center_y += self.move_p2 * paddle_speed

        # Verifica colisões com as raquetes
        self.player1.bounce_ball(self.ball)
        self.player2.bounce_ball(self.ball)

        # Quica nas bordas superior e inferior
        if (self.ball.y < self.y) or (self.ball.top > self.top):
            self.ball.velocity_y *= -1

        # Pontuação quando a bola sai pelas laterais
        if self.ball.x < self.x:
            self.player2.score += 1
            self.serve_ball(vel=(4, 0))
        if self.ball.right > self.width:
            self.player1.score += 1
            self.serve_ball(vel=(-4, 0))

        # Mantém as raquetes dentro dos limites da tela
        self._constrain_paddles()

    def _constrain_paddles(self):
        """Garante que as raquetes não saiam dos limites da tela."""
        self.player1.top = min(self.top, self.player1.top)
        self.player1.y = max(self.y, self.player1.y)
        self.player2.top = min(self.top, self.player2.top)
        self.player2.y = max(self.y, self.player2.y)

    def on_key_down(self, keyboard, keycode, text, modifiers):
        """Handle key press events for continuous movement."""
        key = keycode[1]
        
        # Jogador 1 (W/S)
        if key == 'w':
            self.move_p1 = 1
        elif key == 's':
            self.move_p1 = -1
        
        # Jogador 2 (setas)
        elif key == 'up':
            self.move_p2 = 1
        elif key == 'down':
            self.move_p2 = -1
            
        self._constrain_paddles()
        return True

    def on_key_up(self, keyboard, keycode):
        """Handle key release events to stop movement."""
        key = keycode[1]
        
        # Para o movimento quando as teclas são soltas
        if key in ('w', 's'):
            self.move_p1 = 0
        elif key in ('up', 'down'):
            self.move_p2 = 0
            
        return True

    def on_touch_move(self, touch):
        """Controla as raquetes pelo toque na tela com movimento suavizado."""
        # Jogador 1 (lado esquerdo)
        if touch.x < self.width / 3:
            diff = touch.y - self.player1.center_y
            self.player1.center_y += diff * 0.1  # Movimento suavizado
            
        # Jogador 2 (lado direito)
        if touch.x > self.width - self.width / 3:
            diff = touch.y - self.player2.center_y
            self.player2.center_y += diff * 0.1  # Movimento suavizado
        
        self._constrain_paddles()


class PongApp(App):
    """Aplicação principal do jogo Pong."""
    def build(self):
        game = PongGame()
        game.serve_ball()
        
        # Configura o loop de atualização do jogo (60 FPS)
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        
        # Define cores personalizadas para os jogadores
        game.player1.color_rgb = (1, 0, 0)  # Vermelho
        game.player2.color_rgb = (0, 0, 1)  # Azul

        # Aplica as cores às raquetes
        game.player1.color_instruction.rgb = game.player1.color_rgb
        game.player2.color_instruction.rgb = game.player2.color_rgb

        return game


if __name__ == '__main__':
    PongApp().run()
```