import sdl2, sdl2.sdlimage, mandaw.input, os, sys

class Mandaw:
    def __init__(self, title = None, width = 800, height = 600, bg_color = (0, 0, 0, 255)):
        self.title = title.encode() if title else b"Mandaw"
        self.width = width
        self.height = height
        self.bg_color = bg_color 

        sdl2.SDL_Init(sdl2.SDL_INIT_EVERYTHING)

        self.window = sdl2.SDL_CreateWindow(self.title, sdl2.SDL_WINDOWPOS_CENTERED, sdl2.SDL_WINDOWPOS_CENTERED, self.width, self.height, sdl2.SDL_WINDOW_SHOWN)
        self.renderer = sdl2.SDL_CreateRenderer(self.window, -1, 0)

        self.running = True

        self.icon = "./mandaw/assets/mandaw.png"
        image = sdl2.sdlimage.IMG_Load(self.icon.encode())
        sdl2.SDL_SetWindowIcon(self.window, image)
        sdl2.SDL_FreeSurface(image)

        self.dt = 1.0 / 60

        self.update_dt = 0
        self.update_handlers = []
        self.draw_handlers = []

        self.input = mandaw.input.Input()

    def _update(self, dt):
        self.update_dt += dt
        while self.update_dt > self.dt:
            for update in self.update_handlers:
                update(self.dt)
            self.update_dt -= self.dt

    def _draw(self):
        for draw in self.draw_handlers:
            draw()
        
    def loop(self):
        sdl2.SDL_ShowWindow(self.window)

        current = sdl2.SDL_GetPerformanceCounter()
        freq = sdl2.SDL_GetPerformanceFrequency()

        event = sdl2.SDL_Event()

        while self.running != False:
            while sdl2.SDL_PollEvent(event) != 0:
                if event.type == sdl2.SDL_QUIT:
                    self.running = False
                if event.type == sdl2.SDL_MOUSEMOTION:
                    self.input.update(event)
                if event.type == sdl2.SDL_KEYDOWN:
                    if event.key.keysym.sym == sdl2.SDLK_ESCAPE:
                        self.running = False
                    if event.key.keysym.sym == sdl2.SDLK_F5:
                        os.execl(sys.executable, sys.executable, *sys.argv)

            new = sdl2.SDL_GetPerformanceCounter()
            self._update((new - current) / freq)
            current = new

            sdl2.SDL_RenderClear(self.renderer)
            self._draw()
            sdl2.SDL_SetRenderDrawColor(self.renderer, self.bg_color[0], self.bg_color[1], self.bg_color[2], self.bg_color[3])
            sdl2.SDL_RenderPresent(self.renderer)

        sdl2.SDL_DestroyRenderer(self.renderer)
        sdl2.SDL_DestroyWindow(self.window)
        
        sdl2.SDL_Quit()

    def quit(self):
        self.running = False

    def draw(self, fn):
        self.draw_handlers.append(fn)
        return fn

    def update(self, fn):
        self.update_handlers.append(fn)
        return fn

    def set_icon(self, file):
        image = sdl2.sdlimage.IMG_Load(file.encode())
        sdl2.SDL_SetWindowIcon(self.window, image)
        sdl2.SDL_FreeSurface(image)
