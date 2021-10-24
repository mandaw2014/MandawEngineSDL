from mandaw import Entity, color
import random

class Player(Entity):
    def __init__(self, window):
        super().__init__(
            window,
            width = 20,
            height = 20,
            x = 0,
            y = 0,
            color = color["orange"]
        )

        self.center()
        
        self.window = window

        self.jump_y = 5

        self.speed_x = 1 * random.choice((1, -1))
        self.gravity = 9.81

        self.hit = False

        self.is_jumping = False

        self.direction = 0

    def movement(self, dt):
        self.x += 200 * self.speed_x * dt

        if self.y < 40:
            self.y = 50

        if self.speed_x <= -1:
            self.direction = 0
        if self.speed_x >= 1:
            self.direction = 1

        if self.x >= 780 or self.x <= 0:
            self.speed_x *= -1
            self.hit = True
        else:
            self.hit = False
        
        if self.is_jumping == False:
            self.y += 23 * self.gravity * dt

        self.jump(dt)

    def jump(self, dt):
        if self.is_jumping == False and self.window.input.pressed[self.window.input.keys["SPACE"]]:
            self.is_jumping = True

        if self.is_jumping == True:
            self.y -= 300 * dt
            self.jump_y += 1

            if self.jump_y > 5:
                self.is_jumping = False
                self.jump_y = 0