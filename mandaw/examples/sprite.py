from mandaw import *

mandaw = Mandaw("Sprites!", width = 800, height = 600, bg_color = (0, 0, 0, 255))

sprite = Sprite(window = mandaw, file = "./mandaw/assets/mandaw.png", width = 200, height = 200, x = 0, y = 0)
sprite.center()

@mandaw.draw
def draw():
    sprite.draw()

mandaw.loop()