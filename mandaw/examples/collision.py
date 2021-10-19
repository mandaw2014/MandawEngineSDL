from mandaw import *

mandaw = Mandaw("Collisions!", width = 800, height = 600, bg_color = (0, 0, 0, 255))

player = Entity(window = mandaw, width = 30, height = 30, x = 0, y = 0, color = (255, 255, 255, 255))
player.center()

collision_object_1 = Entity(window = mandaw, width = 20, height = 20, x = 600, y = 300, color = (255, 255, 255, 255))
collision_object_2 = Entity(window = mandaw, width = 20, height = 20, x = 400, y = 500, color = (255, 255, 255, 255))
collision_object_3 = Entity(window = mandaw, width = 20, height = 20, x = 200, y = 300, color = (255, 255, 255, 255))
collision_object_4 = Entity(window = mandaw, width = 20, height = 20, x = 400, y = 100, color = (255, 255, 255, 255))

objects = []

objects.append(collision_object_1)
objects.append(collision_object_2) 
objects.append(collision_object_3) 
objects.append(collision_object_4)

@mandaw.draw
def draw():
    collision_object_1.draw()
    collision_object_2.draw()
    collision_object_3.draw()
    collision_object_4.draw()

    player.draw()

@mandaw.update
def update(dt):
    if mandaw.input.pressed[mandaw.input.keys["UP"]]:
        player.y -= 100 * dt
    if mandaw.input.pressed[mandaw.input.keys["LEFT"]]:
        player.x -= 100 * dt
    if mandaw.input.pressed[mandaw.input.keys["DOWN"]]:
        player.y += 100 * dt
    if mandaw.input.pressed[mandaw.input.keys["RIGHT"]]:
        player.x += 100 * dt

    # Collide with list
    if player.collidelist(objects):
        print("HIT")
    
    # OR, collide with singular object
    if player.collide(collision_object_1):
        collision_object_1.color = color["red"]
    else:
        collision_object_1.color = color["white"]
    
    if player.collide(collision_object_2):
        collision_object_2.color = color["red"]
    else:
        collision_object_2.color = color["white"]

    if player.collide(collision_object_3):
        collision_object_3.color = color["red"]
    else:
        collision_object_3.color = color["white"]

    if player.collide(collision_object_4):
        collision_object_4.color = color["red"]
    else:
        collision_object_4.color = color["white"]

mandaw.loop()