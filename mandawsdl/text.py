from mandawsdl.color import Color
import sdl2, sdl2.ext, sdl2.sdlttf

class Text:
    def __init__(self, window, text, size = 24, color = Color(255, 255, 255)):
        self.text = text
        self.size = size
        self.color = color

        sdl2.sdlttf.TTF_Init()
        sdl2.sdlttf.TTF_Quit()

        font = sdl2.sdlttf.TTF_OpenFont("./assets/font.ttf", self.size)
        sdl2.sdlttf.TTF_CloseFont(font)

        surface = sdl2.sdlttf.TTF_RenderText_Solid(font, self.text, self.color)

if __name__ == "__main__":
    from mandawsdl import *

    mandaw = Mandaw("Text!", 800, 600)

    text = Text(mandaw.world)

    while True:
        mandaw.run()
