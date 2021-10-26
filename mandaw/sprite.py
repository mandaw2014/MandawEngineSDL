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

        self.mirror = None

        self.animations = {}

        self.image = sdlimage.IMG_LoadTexture(self.window.renderer, self.file.encode())
        sdl2.SDL_QueryTexture(self.image, None, None, ctypes.c_int(self.width), ctypes.c_int(self.height))
        self.rect = sdl2.SDL_FRect(self.x, self.y, self.width * 2, self.height * 2)

    def draw(self):
        self.rect = sdl2.SDL_FRect(self.x, self.y, self.width, self.height)

        if self.mirror is None:
            sdl2.SDL_RenderCopyF(self.window.renderer, self.image, None, self.rect)
        elif self.mirror == "x":
            sdl2.SDL_RenderCopyExF(self.window.renderer, self.image, None, self.rect, 0, None, sdl2.SDL_FLIP_HORIZONTAL)
        elif self.mirror == "y":
            sdl2.SDL_RenderCopyExF(self.window.renderer, self.image, None, self.rect, 0, None, sdl2.SDL_FLIP_VERTICAL)

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

    def add_animation(self, animation, name):
        self.animations[name] = {"frames": animation.frames, "length": animation.count, "cooldown": animation.anim_time,
                                 "count": 0, "folder": animation.folder}

    def play_animation(self, name):
        for i in self.animations:
            if i != name:
                self.animations[i]["count"] = 0
            else:
                self.animations[i]["count"] += self.animations[i]["cooldown"]
                if self.animations[i]["count"] >= self.animations[i]["length"]:
                    self.animations[i]["count"] = 0

                if self.width and self.height is None:
                    self.image = sdlimage.IMG_LoadTexture(self.window.renderer, (self.animations[i]["folder"] + "/" + self.animations[i]["frames"][int(self.animations[i]["count"])]).encode())
                else:
                    self.image = sdlimage.IMG_LoadTexture(self.window.renderer, (self.animations[i]["folder"] + "/" + self.animations[i]["frames"][int(self.animations[i]["count"])]).encode())
                    sdl2.SDL_QueryTexture(self.image, None, None, ctypes.c_int(self.width), ctypes.c_int(self.height))
                    self.rect = sdl2.SDL_FRect(self.x, self.y, self.width * 2, self.height * 2)

                self.draw()

    def mirror_x(self):
        self.mirror = "x"
    
    def mirror_y(self):
        self.mirror = "y"

    def mirror_default(self):
        self.mirror = None

if __name__ == "__main__":
    from mandaw import *

    mandaw = Mandaw("Sprites!", 800, 600)

    sprite = Sprite(mandaw, "./mandaw/assets/mandaw.png", 200, 200, 0, 0)
    sprite.draw()

    @mandaw.draw
    def draw():
        sprite.draw()

    mandaw.loop()
