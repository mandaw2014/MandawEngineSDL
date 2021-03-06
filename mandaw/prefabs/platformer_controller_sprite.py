from mandaw import Mandaw, Sprite, Entity

class PlatformerControllerS2D(Sprite):
    def __init__(self, window, sprite, x = 0, y = 0, centered = True):
        super().__init__(
            window,
            file = sprite,
            width = 100,
            height = 100,
            x = x,
            y = y,
        )

        if centered == True:
            self.center()
        else:
            pass
        
        # Window
        self.window = window

        # Player's X Position
        self.pos_x = 0

        # Set the position as a variable
        self.pos = self.window.width / 2 - 15

        self.is_jumping = False
        self.jump_y = 500

        self.direction = None

        self.velocity_y = 1

        self.objects = []

        # Player's speed and maxspeed
        self.speed = 50
        self.maxspeed = 160

        self.ignore_speed = []

    def movement(self, dt):
        # Player movement
        if self.window.input.pressed[self.window.input.keys["A"]]:
            self.pos_x -= self.speed
            self.direction = 0

        if self.window.input.pressed[self.window.input.keys["D"]]:
            self.pos_x += self.speed
            self.direction = 1

        # Momentum
        if self.pos_x >= self.maxspeed:
            self.pos_x = self.maxspeed
        if self.pos_x <= -self.maxspeed:
            self.pos_x = -self.maxspeed

        self.pos += self.pos_x * dt

        # Gravity
        if not self.collidelist(self.objects) and self.is_jumping == False:
            self.y += 4 * self.velocity_y
            self.velocity_y += 2 * dt

        if self.collidelist(self.objects):
            self.velocity_y = 1

            if self.direction == 0 and not self.window.input.pressed[self.window.input.keys["A"]]:
                self.pos_x += 10

                if self.pos_x >= 0:
                    self.pos_x = 0
            
            if self.direction == 1 and not self.window.input.pressed[self.window.input.keys["D"]]:
                self.pos_x -= 10

                if self.pos_x <= 0:
                    self.pos_x = 0

        if not self.collidelist(self.objects):
            if self.direction == 0 and not self.window.input.pressed[self.window.input.keys["A"]]:
                self.pos_x += 0.1

                if self.pos_x >= 0:
                    self.pos_x = 0
            
            if self.direction == 1 and not self.window.input.pressed[self.window.input.keys["D"]]:
                self.pos_x -= 0.1

                if self.pos_x <= 0:
                    self.pos_x = 0

        # Set the x position as the x variable
        self.x = self.pos

        self.jump(dt)

    def jump(self, dt):
        # Jumping
        if self.is_jumping == False and self.window.input.pressed[self.window.input.keys["SPACE"]]:
            self.is_jumping = True
            if not self.collidelist(self.objects):
                self.is_jumping = False

        if self.is_jumping == True:
            self.y -= self.jump_y * dt
            self.jump_y -= 50

            if self.jump_y < -250:
                self.is_jumping = False
                self.jump_y = 500

if __name__ == "__main__":
    mandaw = Mandaw("PlatformerController2D!", 800, 600, (0, 255, 255, 255))

    player = PlatformerControllerS2D(mandaw, "", 0, 0, True)

    ground = Entity(mandaw, 5000, 100, 0, 500, (150, 150, 150, 255))
    ground.center_x()

    player.objects.append(ground)

    @mandaw.draw
    def draw():
        player.draw()
        ground.draw()
    
    @mandaw.update
    def update(dt):
        player.movement(dt)  

    mandaw.loop()