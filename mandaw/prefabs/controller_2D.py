from mandaw import *

class PlatformerController2D(Entity):
    def __init__(self, window, x = 0, y = 0, centered = True):
        super().__init__(
            window,
            width = 15,
            height = 35,
            x = x,
            y = y,
            color = color["orange"]
        )

        if centered == True:
            self.center()
        else:
            pass
        
        self.window = window

        self.pos_x = 0

        self.pos = self.window.width / 2 - 15

        self.is_jumping = False
        self.jump_y = 500

        self.direction = None

        self.velocity_y = 1

        self.objects = []

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

        for i in range(len(self.objects)):
            self.objects[i].x -= self.pos_x * dt

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
                self.pos_x += 1

                if self.pos_x >= 0:
                    self.pos_x = 0
            
            if self.direction == 1 and not self.window.input.pressed[self.window.input.keys["D"]]:
                self.pos_x -= 1

                if self.pos_x <= 0:
                    self.pos_x = 0

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
    mandaw = Mandaw(title = "Platformer!", width = 800, height = 600, bg_color = color["cyan"])

    player = PlatformerController2D(mandaw, x = 0, y = 0, centered = True)

    ground = Entity(mandaw, width = 5000, height = 100, x = 0, y = 500, color = color["lightgray"])
    ground.center_x()

    player.objects.append(ground)

    class Platform(Entity):
        def __init__(self, x, y):
            super().__init__(
                window = mandaw,
                width = 50, 
                height = 10,
                x = x,
                y = y,
                color = color["green"] 
            )

    class JumpPlatform(Entity):
        def __init__(self, x, y):
            super().__init__(
                window = mandaw,
                width = 50, 
                height = 10,
                x = x,
                y = y,
                color = color["orange"]
            )

    class SpeedPlatform(Entity):
        def __init__(self, x, y):
            super().__init__(
                window = mandaw,
                width = 100, 
                height = 10,
                x = x,
                y = y,
                color = color["blue"]
            )

    class FinishBlock(Entity):
        def __init__(self, x, y):
            super().__init__(
                window = mandaw,
                width = 50, 
                height = 10,
                x = x,
                y = y,
                color = color["yellow"]
            )

    center_x = mandaw.width / 2
    center_y = mandaw.height / 2

    # Platforms
    platform = Platform(center_x - 200, center_y + 170)
    platform1 = Platform(center_x - 280, center_y + 140)
    platform2 = Platform(center_x - 360, center_y + 110)
    platform3 = Platform(center_x - 280, center_y + 80)
    platform4 = Platform(center_x - 200, center_y + 50)
    platform5 = Platform(center_x - 120, center_y + 20)

    platform6 = Platform(center_x - 40, center_y - 10)
    platform7 = JumpPlatform(center_x + 40, center_y + 100)
    platform8 = Platform(center_x + 120, center_y - 40)
    platform9 = Platform(center_x + 220, center_y - 40)
    platform10 = JumpPlatform(center_x + 320, center_y - 40)

    platform11 = Platform(center_x + 220, center_y - 220)
    platform12 = SpeedPlatform(center_x + 80, center_y - 220)
    platform13 = SpeedPlatform(center_x + -120, center_y - 220)
    platform14 = SpeedPlatform(center_x + -320, center_y - 220)

    finishBlock = FinishBlock(center_x + -500, center_y - 220)

    player.objects.append(platform)
    player.objects.append(platform1)
    player.objects.append(platform2)
    player.objects.append(platform3)
    player.objects.append(platform4)
    player.objects.append(platform5)
    player.objects.append(platform6)
    player.objects.append(platform7)
    player.objects.append(platform8)
    player.objects.append(platform9)
    player.objects.append(platform10)
    player.objects.append(platform11)
    player.objects.append(platform12)
    player.objects.append(platform13)
    player.objects.append(platform14)
    player.objects.append(finishBlock)

    @mandaw.draw
    def draw():
        player.draw()
        ground.draw()
        
        platform.draw()
        platform1.draw()
        platform2.draw()
        platform3.draw()
        platform4.draw()
        platform5.draw()
        platform6.draw()
        platform7.draw()
        platform8.draw()
        platform9.draw()
        platform10.draw()
        platform11.draw()
        platform12.draw()
        platform13.draw()
        platform14.draw()

        finishBlock.draw()

    @mandaw.update
    def update(dt):
        player.movement(dt)

        if player.collide(ground):
            player.maxspeed = 160
        if player.collide(platform7) or player.collide(platform10):
            player.jump_y = 1000
        elif player.collidelist(player.objects):
            player.jump_y = 500

        if player.collide(platform12) or player.collide(platform13) or player.collide(platform14):
            player.maxspeed = 260

    mandaw.loop()
