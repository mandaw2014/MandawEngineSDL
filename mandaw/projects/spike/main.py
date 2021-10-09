from mandaw import Mandaw 
from player import Player
from spike import Spike

mandaw = Mandaw("Spike!", 800, 600, bg_color = (130, 255, 255, 255))

player = Player(mandaw)

spike1 = Spike(mandaw, player)
spike2 = Spike(mandaw, player)
spike3 = Spike(mandaw, player)
spike4 = Spike(mandaw, player)
spike5 = Spike(mandaw, player)
spike6 = Spike(mandaw, player)

@mandaw.draw
def draw():
    player.draw()

    spike1.draw()
    spike2.draw()
    spike3.draw()
    spike4.draw()
    spike5.draw()
    spike6.draw()

@mandaw.update
def update(dt):
    spike1.update()
    spike2.update()
    spike3.update()
    spike4.update()
    spike5.update()
    spike6.update()

    player.movement(dt)

mandaw.loop()