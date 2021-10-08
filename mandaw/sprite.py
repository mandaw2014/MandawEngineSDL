import sdl2.sdlimage, mandaw

class Sprite(object):
    def __init__(self, window, file, x = 0, y = 0):
        self.window = window
        self.file = file
        self.x = x
        self.y = y

        sdl2.sdlimage.IMG_Init(sdl2.sdlimage.IMG_INIT_PNG)
        self.image = sdl2.sdlimage.IMG_Load(self.file)
        self.entity = mandaw.Entity(window, )