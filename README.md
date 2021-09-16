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
