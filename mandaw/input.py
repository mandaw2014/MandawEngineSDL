import sdl2
import sdl2.ext

class Input:
    def __init__(self):
        self.KEYUP = sdl2.SDL_KEYUP
        self.KEYDOWN = sdl2.SDL_KEYDOWN

        self.UP = sdl2.SDLK_UP
        self.DOWN = sdl2.SDLK_DOWN