import sdl2
import sdl2.ext
from mandaw.color import Color

class GameObject(object):
    def __init__(self, window, width = 20, height = 20, x = 0, y = 0, color = Color(255, 255, 255)):
        self.entity = sdl2.ext.Entity(world = window.world)

        self.window = window
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        self.color = color

        self.entity.sprite = self.entity.world.factory.from_color(self.color, (0, 0))
    
    def draw(self):
        self.entity.sprite = self.entity.world.factory.from_color(self.color, (self.width, self.height))
        self.entity.sprite.position = self.x, self.y

    def collide(self, rect):
        left, top, right, bottom = self.entity.sprite.area

        try:
            if type(rect) != list:
                bleft, btop, bright, bbottom = rect.entity.sprite.area

                return(bleft < right and bright > left and btop < bottom and bbottom > top)
            
            elif type(rect) == list:
                for i in range(len(rect)):
                    bleft, btop, bright, bbottom = rect[i].entity.sprite.area

                    return(bleft < right and bright > left and btop < bottom and bbottom > top)

        except:
            raise AttributeError("MandawError: Object was not a GameObject or a list of GameObjects :(")

    def center(self):
        self.x = int(self.window.width / 2) - int(self.width / 2)
        self.y = int(self.window.height / 2) - int(self.height / 2)

    def center_x(self):
        self.x = int(self.window.width / 2) - int(self.width / 2)

    def center_y(self):
        self.y = int(self.window.height / 2) - int(self.height / 2)
