from mandawsdl import *

mandaw = Mandaw("Classes!", 800, 600)

class Cube(GameObject):
    def __init__(self, world):
        super().__init__(
            world = world,
            width = 20,
            height = 20,
            x = 0,
            y = 0,
            color = Color(0, 255, 255)
        )

        self.center()

cube = Cube(mandaw.world)

while True:
    cube.draw()
    mandaw.run()