import sdl2
import sdl2.ext
from mandaw.input import Input

class Mandaw:
    def __init__(self, title = "Mandaw", width = 800, height = 600, bg_color = sdl2.ext.Color(0, 0, 0)):
        self.title = title
        self.width = width
        self.height = height
        self.bg_color = bg_color

        sdl2.ext.init()

        self.running = True

        self.window = sdl2.ext.Window(self.title, size = (self.width, self.height))
        self.window.show()

        self.window.bg_color = bg_color

        self.world = sdl2.ext.World()
        self.world.width = width
        self.world.height = height

        self.factory = sdl2.ext.SpriteFactory(sdl2.ext.SOFTWARE)

        self.sprite_renderer = SoftwareRenderer(self.window)
        self.world.add_system(self.sprite_renderer)

        self.input = Input()

    def run(self):
        events = sdl2.ext.get_events()
        for event in events:
            if event.type == sdl2.SDL_QUIT:
                quit()

        self.world.process()

class SoftwareRenderer(sdl2.ext.SoftwareSpriteRenderSystem):
    def __init__(self, window):
        super().__init__(window)

    def render(self, components):
        sdl2.ext.fill(self.surface, sdl2.ext.Color(0, 0, 0))
        super().render(components)