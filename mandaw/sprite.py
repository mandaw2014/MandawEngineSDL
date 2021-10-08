import sdl2, sdl2.ext

class Sprite:
    def __init__(self, window, image, x = 0, y = 0):
        self.entity = sdl2.ext.Entity(world = window.world)

        self.window = window
        self.image = image
        self.x = x
        self.y = y

        self.entity.sprite = self.window.factory.from_image(self.image)
        self.spriterenderer = self.window.factory.create_sprite_render_system(self.window.window)

    def draw(self):
        self.spriterenderer.render(self.entity.sprite)
        self.entity.sprite.position = self.x, self.y

    def collide(self, sprite):
        left, top, right, bottom = self.entity.sprite.area
        bleft, btop, bright, bbottom = sprite.entity.sprite.area

        return(bleft < right and bright > left and btop < bottom and bbottom > top)

    def collidelist(self, sprite):
        collisions = [True if self.collide(sprite[i]) else False for i in range(len(sprite))]
        return any(collisions)