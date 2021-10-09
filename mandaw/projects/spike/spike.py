from mandaw import Entity, color
import random

class Spike(Entity):
    def __init__(self, window, player):
        super().__init__(
            window,
            15, 15, 0, 0,
            color["red"]
        )

        self.player = player

        self.reset()

    def update(self):
        if self.player.collide(self):
            self.player.center()
            self.reset()

        if self.player.hit:
            if self.player.direction == 0:
                self.reset()
            
            if self.player.direction == 1:
                self.reset()

    def reset(self):
        if self.player.direction == 0:
            self.x = 785
            self.y = random.randint(0, 600)
        
        if self.player.direction == 1:
            self.x = 0
            self.y = random.randint(0, 600)