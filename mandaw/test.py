from mandaw import Mandaw, Entity

mandaw = Mandaw("Test")

entity = Entity(mandaw, 100, 100, 250, 150)
entity1 = Entity(mandaw, 100, 100, 0, 0)

@mandaw.draw
def draw():
    entity.draw()
    entity1.draw()

@mandaw.update
def update(dt):
    if mandaw.input.pressed[mandaw.input.keys["W"]]:
        entity.y -= 100 * dt
    if mandaw.input.pressed[mandaw.input.keys["A"]]:
        entity.x -= 100 * dt
    if mandaw.input.pressed[mandaw.input.keys["S"]]:
        entity.y += 100 * dt
    if mandaw.input.pressed[mandaw.input.keys["D"]]:
        entity.x += 100 * dt

    if mandaw.input.pressed[mandaw.input.keys["UP"]]:
        entity1.y -= 100 * dt
    if mandaw.input.pressed[mandaw.input.keys["LEFT"]]:
        entity1.x -= 100 * dt
    if mandaw.input.pressed[mandaw.input.keys["DOWN"]]:
        entity1.y += 100 * dt
    if mandaw.input.pressed[mandaw.input.keys["RIGHT"]]:
        entity1.x += 100 * dt

    if entity.collide(entity1):
        print("Collide!")

mandaw.loop()