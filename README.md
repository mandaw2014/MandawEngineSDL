# MandawEngine
A 2D Python GameEngine Made With PySDL2

Discord: https://discord.gg/MPPqj9PNt3

# Installation
To install:
Download the zip: Code->Download Zip
Extract it
Go into the extracted folder and Type in CMD or Terminal:
```
pip install setup.py
```

# Creating A Window
First, import mandaw
```py
from mandaw import *
```
Call Mandaw
```py
mandaw = Mandaw(title = "Window!", width = 800, height = 600, bg_color = (0, 0, 0, 255))
```
To run it, type
```py
mandaw.loop()
```

# Creating A Square
Here is what we have so far
```py
from mandaw import *

mandaw = Mandaw(title = "Window!", width = 800, height = 600, bg_color = (0, 0, 0, 255))

mandaw.loop()
```
To create a square, type
```py
square = Entity(window = mandaw, width = 20, height = 20, x = 0, y = 0, color = (255, 255, 255, 255))
```
Center it with
```py
square.center()
```
Then draw it
```py
@mandaw.draw
def draw():
    square.draw()
```
Like this
```py
from mandaw import *

mandaw = Mandaw(title = "Window!", width = 800, height = 600, bg_color = (0, 0, 0, 255))

square = Entity(window = mandaw, width = 20, height = 20, x = 0, y = 0, color = (255, 255, 255, 255))
square.center()

@mandaw.draw
def draw():
    square.draw()

mandaw.loop()
```
