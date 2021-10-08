from mandaw import *
import random

mandaw = Mandaw("Pong!", width = 800, height = 600)

class Paddle(Entity):
    def __init__(self, x, y):
        super().__init__(
            mandaw,
            width = 20,
            height = 100,
            x = x,
            y = y,
        )

        self.ball = None

    def player_movement(self, dt):
        if mandaw.input.pressed[mandaw.input.keys["UP"]]:
            self.y -= 200 * dt
        if mandaw.input.pressed[mandaw.input.keys["DOWN"]]:
            self.y += 200 * dt

        if self.y >= mandaw.height - 30:
            self.y = mandaw.height - 30
        if self.y <= -60:
            self.y = -60
        
    def opponent_movement(self, dt):
        if self.y < self.ball.y:
            self.y += 180 * dt
        if self.y > self.ball.y:
            self.y -= 180 * dt

        if self.y >= mandaw.height - 30:
            self.y = mandaw.height - 30
        if self.y <= -60:
            self.y = -60

class Ball(Entity):
    def __init__(self):
        super().__init__(
            mandaw,
            width = 20,
            height = 20,
            x = 0,
            y = 0
        )

        self.center()

        self.ball_speed_x = 1 * random.choice((1, -1))
        self.ball_speed_y = 1 * random.choice((1, -1))

    def ball_movement(self, dt):
        self.x += 200 * self.ball_speed_x * dt
        self.y += 200 * self.ball_speed_y * dt

        if self.y <= 2 or self.y >= mandaw.height - 20:
            self.ball_speed_y *= -1
        if self.x <= 0:
            self.reset()
        elif self.x >= mandaw.width:
            self.reset()

    def reset(self):
        self.center()
        self.ball_speed_y *= random.choice((1, -1))
        self.ball_speed_x *= random.choice((1, -1))

player1 = Paddle(x = 0, y = 250)
player2 = Paddle(x = 780, y = 250)

ball = Ball()

player2.ball = ball

@mandaw.update
def update(dt):
    if ball.collide(player1) or ball.collide(player2):
        ball.ball_speed_x *= -1

    player1.player_movement(dt)
    player2.opponent_movement(dt)
    ball.ball_movement(dt)

@mandaw.draw
def draw():
    player1.draw()
    player2.draw()
    ball.draw()

mandaw.loop()