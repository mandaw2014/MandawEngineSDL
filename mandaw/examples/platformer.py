from mandaw import *

mandaw = Mandaw("Platformer!", width = 800, height = 600)
mandaw.bg_color = mandaw.color["cyan"]

class PlatformerController2D(GameObject):
    def __init__(self, world, x = 0, y = 0, centered = True):
        super().__init__(
            world,
            width = 15,
            height = 35,
            x = x,
            y = y,
            color = Color(255, 165, 0)
        )

        self.attribute.window = world

        if centered == True:
            self.center()
        else:
            pass

        # Player's X Position
        self.attribute.pos_x = 0

        # Set the position as a variable
        self.attribute.pos = self.attribute.window.width / 2 - 15

        self.attribute.is_jumping = False
        self.attribute.jump_y = 5

        self.attribute.direction = None

        self.attribute.velocity_y = 1

        # Player's speed and maxspeed
        self.attribute.speed = 0.1
        self.attribute.maxspeed = 2

        self.attribute.ground = None
        self.attribute.ignore_speed = []

    def movement(self):
        # Player movement
        if mandaw.input.pressed[mandaw.input.keys["A"]]:
            self.attribute.pos_x -= self.attribute.speed * mandaw.dt
            self.attribute.direction = 0

        if mandaw.input.pressed[mandaw.input.keys["D"]]:
            self.attribute.pos_x += self.attribute.speed * mandaw.dt
            self.attribute.direction = 1

        # Momentum
        if self.attribute.pos_x >= self.attribute.maxspeed:
            self.attribute.pos_x = self.attribute.maxspeed
        if self.attribute.pos_x <= -self.attribute.maxspeed:
            self.attribute.pos_x = -self.attribute.maxspeed

        self.attribute.pos += int(self.attribute.pos_x)

        # Gravity
        if not self.collide(self.attribute.ground) and self.attribute.is_jumping == False:
            self.position.y += 3 * int(self.attribute.velocity_y)
            self.attribute.velocity_y += 0.1

        if self.collide(self.attribute.ground):
            self.attribute.velocity_y = 1

            if self.attribute.direction == 0 and not mandaw.input.pressed[mandaw.input.keys["A"]]:
                self.attribute.pos_x += 10

                if self.attribute.pos_x >= 0:
                    self.attribute.pos_x = 0
            
            if self.attribute.direction == 1 and not mandaw.input.pressed[mandaw.input.keys["D"]]:
                self.attribute.pos_x -= 10

                if self.attribute.pos_x <= 0:
                    self.attribute.pos_x = 0

        if not self.collide(self.attribute.ground):
            if self.attribute.direction == 0 and not mandaw.input.pressed[mandaw.input.keys["A"]]:
                self.attribute.pos_x += 0.1 * mandaw.dt

                if self.attribute.pos_x >= 0:
                    self.attribute.pos_x = 0
            
            if self.attribute.direction == 1 and not mandaw.input.pressed[mandaw.input.keys["D"]]:
                self.attribute.pos_x -= 0.1 * mandaw.dt

                if self.attribute.pos_x <= 0:
                    self.attribute.pos_x = 0

        # Set the x position as the x variable
        self.position.x = int(self.attribute.pos)

        self.jump()

    def jump(self):
        # Jumping
        if self.attribute.is_jumping == False and mandaw.input.pressed[mandaw.input.keys["SPACE"]]:
            self.attribute.is_jumping = True
            if not self.collide(self.attribute.ground):
                self.attribute.is_jumping = False

        if self.attribute.is_jumping == True:
            self.position.y -= self.attribute.jump_y
            self.attribute.jump_y -= 1

            if self.attribute.jump_y < -5:
                self.attribute.is_jumping = False
                self.attribute.jump_y = 10

player = PlatformerController2D(mandaw.world, 0, 0, True)

ground = GameObject(mandaw.world, 5000, 100, 0, 500, color = Color(195, 195, 195))
ground.center_x()

player.attribute.ground = ground

while True:
    player.draw()
    ground.draw()

    player.movement()

    mandaw.run()