import sdl2.ext

class Color(sdl2.ext.Color):
    def __init__(self, r, g, b):
        super().__init__(
            r, g, b
        )