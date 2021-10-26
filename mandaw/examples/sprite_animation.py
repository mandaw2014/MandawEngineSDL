from mandaw import *

mandaw = Mandaw()

character = Sprite(mandaw, "assets/adventurer.png", 200, 200, 0, 0)
character.center()

idle = Animation("assets/idle1", 0.14)
run = Animation("assets/normal-run", 0.14)

character.add_animation(idle, "idle")
character.add_animation(run, "run")

@mandaw.draw
def draw():
    character.draw()

@mandaw.update
def update(dt):
    if mandaw.input.pressed[mandaw.input.keys["D"]]:
        character.play_animation("run")
        character.x += 60 * 5 * dt
        character.mirror = None

    elif mandaw.input.pressed[mandaw.input.keys["A"]]:
        character.play_animation("run")
        character.x -= 60 * 5 * dt
        character.mirror = "x"

    else:
        character.play_animation("idle")

mandaw.loop()