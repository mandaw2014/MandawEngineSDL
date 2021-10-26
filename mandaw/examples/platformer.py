from mandaw import *
from mandaw.prefabs.platformer_controller import PlatformerController2D

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

finishBlock = FinishBlock(center_x + -400, center_y - 220)

player.objects.append(ground)
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

    if player.collide(platform7) or player.collide(platform10):
        player.jump_y = 1000
    elif player.collidelist(player.objects):
        player.jump_y = 500

    if player.collide(platform12) or player.collide(platform13) or player.collide(platform14):
        player.maxspeed = 260

    if player.collide(ground):
        player.maxspeed = 160

mandaw.loop()
