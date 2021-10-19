from mandaw import *

mandaw = Mandaw("Classes!", width = 800, height = 600, bg_color = (0, 0, 0, 255))

class Square(Entity):
    def __init__(self, window):
        super().__init__(
            window = window,
            width = 20,
            height = 20,
            x = 0,
            y = 0,
            color = color["white"]
        )

        self.center()

square = Square(mandaw)

@mandaw.draw
def draw():
    square.draw()

mandaw.loop()