from mandawsdl import *

mandaw = Mandaw("Collisions!", 800, 600)

player = GameObject(mandaw.world, 30, 30, 0, 0)
player.center()

class CollisionObject(GameObject):
    def __init__(self, world, x, y):
        super().__init__(
            world,
            width = 25,
            height = 25,
            x = x,
            y = y
        )

object1 = CollisionObject(mandaw.world, 600, 300)
object2 = CollisionObject(mandaw.world, 200, 300)
object3 = CollisionObject(mandaw.world, 400, 100)
object4 = CollisionObject(mandaw.world, 400, 400)

while True:
    if mandaw.input.pressed[mandaw.input.keys["UP"]]:
        player.position.y -= 1
    if mandaw.input.pressed[mandaw.input.keys["LEFT"]]:
        player.position.x -= 1
    if mandaw.input.pressed[mandaw.input.keys["DOWN"]]:
        player.position.y += 1
    if mandaw.input.pressed[mandaw.input.keys["RIGHT"]]:
        player.position.x += 1

    if player.collide(object1):
        object1.attribute.color = Color(255, 0, 0)
    else:
        object1.attribute.color = Color(255, 255, 255)

    if player.collide(object2):
        object2.attribute.color = Color(255, 0, 0)
    else:
        object2.attribute.color = Color(255, 255, 255)

    if player.collide(object3):
        object3.attribute.color = Color(255, 0, 0)
    else:
        object3.attribute.color = Color(255, 255, 255)

    if player.collide(object4):
        object4.attribute.color = Color(255, 0, 0)
    else:
        object4.attribute.color = Color(255, 255, 255)

    object1.draw()
    object2.draw()
    object3.draw()
    object4.draw()

    player.draw()

    mandaw.run()