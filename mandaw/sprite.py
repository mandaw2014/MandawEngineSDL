from sdl2 import sdlimage
import sdl2, ctypes

class Sprite(object):
    def __init__(self, window, file, width = 200, height = 200, x = 0, y = 0):
        self.window = window
        self.file = file
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        self.image = sdlimage.IMG_LoadTexture(self.window.renderer, self.file.encode())
        sdl2.SDL_QueryTexture(self.image, None, None, ctypes.c_int(self.width), ctypes.c_int(self.height))
        self.rect = sdl2.SDL_FRect(self.x, self.y, self.width * 2, self.height * 2)

    def draw(self):
        self.rect = sdl2.SDL_FRect(self.x, self.y, self.width, self.height)
        sdl2.SDL_RenderCopyF(self.window.renderer, self.image, None, self.rect)
        self.rect = sdl2.SDL_FRect(self.x, self.y, self.width, self.height)

    def collide(self, rect):
            leftA = self.rect.x
            rightA = self.rect.x + self.rect.w
            topA = self.rect.y
            bottomA = self.rect.y + self.rect.h

            leftB = rect.rect.x
            rightB = rect.rect.x + rect.rect.w
            topB = rect.rect.y
            bottomB = rect.rect.y + rect.rect.h

            if bottomA <= topB:
                return False
            
            if topA >= bottomB:
                return False
            
            if rightA <= leftB:
                return False
            
            if leftA >= rightB:
                return False
            
            return True

    def collidelist(self, rect_list):
        collisions = [True if self.collide(rect_list[i]) else False for i in range(len(rect_list))]
        return any(collisions)

    def center(self):
        self.x = self.window.width / 2 - self.width / 2
        self.y = self.window.height / 2 - self.height / 2

    def center_x(self):
        self.x = self.window.width / 2 - self.width / 2

    def center_y(self):
        self.y = self.window.height / 2 - self.height / 2

if __name__ == "__main__":
    from mandaw import *

    mandaw = Mandaw("Sprites!", 800, 600)

    sprite = Sprite(mandaw, "./mandaw/assets/mandaw.png", 200, 200, 0, 0)
    sprite.draw()

    @mandaw.draw
    def draw():
        sprite.draw()

    mandaw.loop()