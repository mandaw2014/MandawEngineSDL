# MandawEngine
A 2D Python GameEngine Made With PySDL2

Discord: https://discord.gg/MPPqj9PNt3

# Installation
To install:
1. Download the zip
2. Extract the zip
3. On Windows: Double click the install.bat
4. On Mac and Linux: In Terminal, navigate to the folder where you extracted the zip and type
```py
python3 setup.py install
```

# Creating A Window
First, import mandaw
```py
from mandaw import *
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
from mandaw import *

mandaw = Mandaw(title = "Mandaw", width = 800, height = 600)

while True:
    mandaw.run()
```
To create a square, type
```py
sqaure = GameObject(mandaw.world, size = (20, 20), x = 390, y = 290)
```
Like this
```py
from mandaw import *

mandaw = Mandaw(title = "Mandaw", width = 800, height = 600)

sqaure = GameObject(mandaw.world, size = (20, 20), x = 390, y = 290)

while True:
    mandaw.run()
```
