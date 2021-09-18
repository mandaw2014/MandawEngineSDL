# MandawEngineSDL
A 2D Python GameEngine Made With PySDL2

Discord: https://discord.gg/MPPqj9PNt3

# Installation
To install:
1. Download the zip
2. Extract the zip
3. On Windows: Double click the install.bat (If that doesn't work, follow the step below)
4. On Mac and Linux: In Terminal, navigate to the folder where you extracted the zip and type
```py
python3 setup.py install
```

# Creating A Window
First, import mandaw
```py
from mandawsdl import *
```
Call Mandaw
```py
mandaw = Mandaw(title = "Mandaw", width = 800, height = 600)
```
To run it, type
```py
while True:
    mandaw.run()
```

# Creating A Square
Here is what we have so far
```py
from mandawsdl import *

mandaw = Mandaw(title = "Mandaw", width = 800, height = 600)

while True:
    mandaw.run()
```
To create a square, type
```py
square = GameObject(mandaw.world, width = 20, height = 20, color = Color(255, 0, 0))
```
Then draw it
```py
while True:
    square.draw()
    ...
```
Like this
```py
from mandawsdl import *

mandaw = Mandaw(title = "Mandaw", width = 800, height = 600)

square = GameObject(mandaw.world, width = 20, height = 20, color = Color(255, 0, 0))

while True:
    square.draw()
    mandaw.run()
```

# Classes in MandawEngineSDL
Our starting template
```py
from mandawsdl import *

mandaw = Mandaw("Classes!", 800, 600)

while True:
    mandaw.run()
```
To make a GameObject class in MandawEngineSDL, you have to include 'world' in the `__init__` function
```py
class Cube(GameObject):
    def __init__(self, world):
```
Next, make the `super().__init__()`
```py
super().__init__(
    world = world,
    width = 20,
    height = 20,
    x = 0,
    y = 0,
    color = Color(0, 255, 255)
)
```
In the `__init__` funtion, you can also include
```py
self.center()
```
When you want to call the class, you do
```py
cube = Cube(mandaw.world)
```
And don't forget to draw it
```py
while True:
    cube.draw()
```
Full Code:
```py
from mandawsdl import *

mandaw = Mandaw("Classes!", 800, 600)

class Cube(GameObject):
    def __init__(self, world):
        super().__init__(
            world = world,
            width = 20,
            height = 20,
            x = 0,
            y = 0,
            color = Color(0, 255, 255)
        )

        self.center()

cube = Cube(mandaw.world)

while True:
    cube.draw()
    mandaw.run()
```
