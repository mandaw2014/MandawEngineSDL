import sdl2
import sdl2.ext
from mandawsdl.color import Color

class GameObject(sdl2.ext.Entity):
    def __init__(self, world, width = 20, height = 20, x = 0, y = 0, color = Color(255, 255, 255)):
        self.world = world

        self.position = Position(x, y)
        self.size = Size(width, height)

        self.attribute = Attribute()
        self.attribute.color = color

        self.sprite = self.world.factory.from_color(self.attribute.color, (0, 0))
    
    def draw(self):
        self.sprite = self.world.factory.from_color(self.attribute.color, (self.size.width, self.size.height))
        self.sprite.position = self.position.x, self.position.y

    def collide(self, rect):
        left, top, right, bottom = self.sprite.area
        bleft, btop, bright, bbottom = rect.sprite.area

        return(bleft < right and bright > left and btop < bottom and bbottom > top)

    def center(self):
        self.position.x = int(self.world.width / 2) - int(self.size.width / 2)
        self.position.y = int(self.world.height / 2) - int(self.size.height / 2)

    def center_x(self):
        self.position.x = int(self.world.width / 2) - int(self.size.width / 2)

    def center_y(self):
        self.position.y = int(self.world.height / 2) - int(self.size.height / 2)

class Position(object):
    def __init__(self, x, y):
        self.position = x, y
        self.x = x
        self.y = y

class Size(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.size = (self.width, self.height)

class Attribute(object):
    def __init__(self):
        pass