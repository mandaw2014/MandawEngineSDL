from mandawsdl import *

mandaw = Mandaw("Mandaw", 800, 600)

square = GameObject(mandaw.world, (20, 20), 390, 290)

while True:
    mandaw.run()
