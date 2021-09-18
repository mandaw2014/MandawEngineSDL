from mandawsdl import *
import random

mandaw = Mandaw("Pong", 800, 600)

BLACK = Color(0, 0, 0)
WHITE = Color(255, 255, 255)

class Paddle(GameObject):
    def __init__(self, world, x, y):
        super().__init__(
            world,
            width = 20,
            height = 100,
            x = x,
            y = y,
            color = WHITE
        )

        self.attribute.ball = None

    def player_movement(self):
        if mandaw.input.pressed[mandaw.input.keys["UP"]]:
            self.position.y -= 2
        if mandaw.input.pressed[mandaw.input.keys["DOWN"]]:
            self.position.y += 2

        if self.position.y >= mandaw.height - 30:
            self.position.y = mandaw.height - 30
        if self.position.y <= -60:
            self.position.y = -60

    def opponent_movement(self):
        if self.position.y < self.attribute.ball.position.y:
            self.position.y += 2
        if self.position.y > self.attribute.ball.position.y:
            self.position.y -= 2

        if self.position.y >= mandaw.height - 30:
            self.position.y = mandaw.height - 30
        if self.position.y <= -60:
            self.position.y = -60

class Ball(GameObject):
    def __init__(self, world, x, y):
        super().__init__(
            world,
            width = 20,
            height = 20,
            x = x,
            y = y,
            color = WHITE
        )

        self.attribute.ball_speed_x = 1 * random.choice((1, -1))
        self.attribute.ball_speed_y = 1 * random.choice((1, -1))

    def ball_movement(self):
        self.position.x += 2 * self.attribute.ball_speed_x
        self.position.y += 2 * self.attribute.ball_speed_y

        # Collisions
        if self.position.y <= 2 or self.position.y >= mandaw.height - 20:
            self.attribute.ball_speed_y *= -1
        if self.position.x <= 0:
            self.reset()
        elif self.position.x >= mandaw.width:
            self.reset()

    def reset(self):
        self.center()
        self.attribute.ball_speed_y *= random.choice((1, -1))
        self.attribute.ball_speed_x *= random.choice((1, -1))

player = Paddle(mandaw.world, x = 0, y = 250)
player1 = Paddle(mandaw.world, x = 780, y = 250)

ball = Ball(mandaw.world, x = 390, y = 290)
ball.center()

player1.attribute.ball = ball

while True:
    player.player_movement()
    player1.opponent_movement()

    if ball.collide(player) or ball.collide(player1):
        ball.attribute.ball_speed_x *= -1

    ball.ball_movement()

    player.draw()
    player1.draw()
    ball.draw()
    mandaw.run()