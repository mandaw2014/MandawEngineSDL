import sdl2, math

class Entity(object):
    def __init__(self, window, width = 20, height = 20, x = 0, y = 0, color = (255, 255, 255, 255)):
        self.window = window
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.color = color

        self.rect = sdl2.SDL_FRect(self.x, self.y, self.width, self.height)

    def draw(self):
        sdl2.SDL_SetRenderDrawColor(self.window.renderer, self.color[0], self.color[1], self.color[2], self.color[3])
        self.rect = sdl2.SDL_FRect(self.x, self.y, self.width, self.height)

        sdl2.SDL_RenderDrawRectF(self.window.renderer, self.rect)
        sdl2.SDL_RenderFillRectF(self.window.renderer, self.rect)

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

def distance(rect1, rect2):
    return (round(math.sqrt((rect2.x - rect1.x) ** 2 + (rect2.y - rect1.y) ** 2), 2)) / 10