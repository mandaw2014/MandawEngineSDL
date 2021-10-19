import sdl2, sdl2.sdlttf

class Text(object):
    def __init__(self, window, text = None, size = 100, x = 0, y = 0, color = (255, 255, 255, 255)):
        self.window = window
        self.text = text
        self.size = size
        self.x = x
        self.y = y
        self.color = color
        
        self.font = sdl2.sdlttf.TTF_OpenFont(b"./mandaw/assets/font.ttf", self.size)
        
        self.surface = sdl2.sdlttf.TTF_RenderText_Solid(self.font, self.text.encode(), sdl2.SDL_Color(255, 255, 255, 255))
        self.texture = sdl2.SDL_CreateTextureFromSurface(self.window.renderer, self.surface)
        
        self.rect = sdl2.SDL_FRect(self.x, self.y, 20, 20)

    def draw(self):
        self.rect = sdl2.SDL_FRect(self.x, self.y, self.size, self.size / 2)
        sdl2.SDL_RenderCopyF(self.window.renderer, self.texture, None, self.rect)
        self.rect = sdl2.SDL_FRect(self.x, self.y, self.size, self.size / 2)