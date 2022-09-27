# CircuitPython
This repository will actually serve as a aid to help you get started with your own template.  You should copy the raw form of this readme into your own, and use this template to write your own.  If you want to draw inspiration from other classmates, feel free to check [this directory of all students!](https://github.com/chssigma/Class_Accounts).
## Table of Contents
* [Table of Contents](#TableOfContents)
* [Hello_CircuitPython](#Hello_CircuitPython)
* [CircuitPython_Servo](#CircuitPython_Servo)
* [CircuitPython_LCD](#CircuitPython_LCD)
* [NextAssignmentGoesHere](#NextAssignment)
---

## Hello_CircuitPython

### Description & Code
Make the LED blink.

```python
import board #importing files
import neopixel
import time
import random 

dot = neopixel.NeoPixel(board.NEOPIXEL, 1) #creates name(dot) for neopixels
dot.brightness =  .1 #sets neopixel brightness

print("Make it red!")

r = random.randint(0,255) #random integer between 0-225 for r(red)
g = random.randint(0,255) #random integer between 0-225 for g(green)
b = random.randint(0,255) #random integer between 0-225 for b(blue)
rgb = [r,g,b] #sets rgb value for random integers

if (r>200): #if r>200 g+b<80 in order to get more solid colors, less white
    g + b < 80

if (g>200): #same principle except for green
    r + b < 80

if (b>200): #same principle for these two except for blue
    g + r < 80

while True:
    dot.fill((rgb)) #make led randomly assigned rgb color
    time.sleep(.5)
    dot.fill((0,0,0)) 
    time.sleep(0.5)
```
### Evidence
https://user-images.githubusercontent.com/91289646/192608483-b7759c1c-ec20-432e-8f1a-45b8bb5374d6.MOV

### Wiring
No wiring is required for this assignement.

### Reflection
Given that this was my first circuitpython assignemnt generally eveything was somewhat difficult given that it was all extremely new to me. I had to make sure I imoported all the files I use in this code. I had to look up the syntax required to get a random RGB value which was fairly easy. I also had to add lines 16-23 to the code beause I kept getting RGB values that made the LED all very dull colors.




## CircuitPython_Servo

### Description & Code

```python
Code goes here

```

### Evidence

Pictures / Gifs of your work should go here.  You need to communicate what your thing does.

### Wiring

### Reflection




## CircuitPython_LCD

### Description & Code

```python
Code goes here

```

### Evidence

Pictures / Gifs of your work should go here.  You need to communicate what your thing does.

### Wiring

### Reflection





## NextAssignment

### Description & Code

```python
Code goes here

```

### Evidence

### Wiring

### Reflection
