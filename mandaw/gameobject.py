import sdl2
import sdl2.ext

class GameObject(sdl2.ext.Entity):
    def __init__(self, world, size = (0, 0), x = 0, y = 0, color = sdl2.ext.Color(255, 255, 255)):
        self.size = size
        self.x = x
        self.y = y
        
        self.world = world

        self.color = color

        factory = sdl2.ext.SpriteFactory(sdl2.ext.SOFTWARE)
        self.sprite = factory.from_color(self.color, size)

        self.sprite.position = x, y