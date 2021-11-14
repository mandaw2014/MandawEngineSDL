from mandaw import *

mandaw = Mandaw()

text = Text(mandaw, "Hello!", "./assets/font.ttf", 24, 100, 0)

@mandaw.draw
def draw():
    text.draw()

mandaw.loop()