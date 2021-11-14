import sdl2, sdl2.sdlmixer

class Audio:
    def __init__(self, filename, loop = 0):
        rate = 22050
        format = sdl2.AUDIO_S16SYS
        channels = 2
        buffers = 4096

        if sdl2.sdlmixer.Mix_OpenAudio(rate, format, channels, buffers) != 0:
            return
        
        self.loop = loop
        self.audio = sdl2.sdlmixer.Mix_LoadWAV(filename.encode())

    def play(self):
        sdl2.sdlmixer.Mix_PlayChannel(-1, self.audio, self.loop)