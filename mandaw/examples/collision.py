from mandaw import *

mandaw = Mandaw("Collisions!", 800, 600)

player = GameObject(mandaw, 30, 30, 0, 0)
player.center()

class CollisionObject(GameObject):
    def __init__(self, x, y):
        super().__init__(
            mandaw,
            width = 25,
            height = 25,
            x = x,
            y = y
        )

object1 = CollisionObject(600, 300)
object2 = CollisionObject(200, 300)
object3 = CollisionObject(400, 100)
object4 = CollisionObject(400, 400)

while True:
    if mandaw.input.pressed[mandaw.input.keys["UP"]]:
        player.y -= 1
    if mandaw.input.pressed[mandaw.input.keys["LEFT"]]:
        player.x -= 1
    if mandaw.input.pressed[mandaw.input.keys["DOWN"]]:
        player.y += 1
    if mandaw.input.pressed[mandaw.input.keys["RIGHT"]]:
        player.x += 1

    if mandaw.input.pressed[mandaw.input.keys["G"]]:
        player.center()

    if player.collide(object1):
        object1.color = Color(255, 0, 0)
    else:
        object1.color = Color(255, 255, 255)
    if player.collide(object2):
        object2.color = Color(255, 0, 0)
    else:
        object2.color = Color(255, 255, 255)
    if player.collide(object3):
        object3.color = Color(255, 0, 0)
    else:
        object3.color = Color(255, 255, 255)
    if player.collide(object4):
        object4.color = Color(255, 0, 0)
    else:
        object4.color = Color(255, 255, 255)

    object1.draw()
    object2.draw()
    object3.draw()
    object4.draw()

    player.draw()

    mandaw.run()
