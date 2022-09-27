# CircuitPython
This repository will actually serve as a aid to help you get started with your own template.  You should copy the raw form of this readme into your own, and use this template to write your own.  If you want to draw inspiration from other classmates, feel free to check [this directory of all students!](https://github.com/chssigma/Class_Accounts).
## Table of Contents
* [Table of Contents](#TableOfContents)
* [Hello_CircuitPython](#Hello_CircuitPython)
* [CircuitPython_Servo](#CircuitPython_Servo)
* [CircuitPython Distance Sensor](#CircuitPyhton_Distance_Sensor)
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
Make a 180 degree servo spin back and forth.

```python
import time #importing files
import board
import pwmio
from adafruit_motor import servo

# create a PWMOut object on Pin 9.
pwm = pwmio.PWMOut(board.D9, duty_cycle=2 ** 20, frequency=40)

# Create a servo object, my_servo.
my_servo = servo.Servo(pwm)

while True:
    for angle in range(0, 180, 5):  # 0 - 180 degrees, 5 degrees at a time forward.
        my_servo.angle = angle
        time.sleep(0.05)
    for angle in range(180, 0, -5): # 180 - 0 degrees, 5 degrees at a time backward.
        my_servo.angle = angle
        time.sleep(0.05)
```

### Evidence
Possibly inaccessible video of my servo spinning.
https://cvilleschools.instructure.com/courses/37129/assignments/493862/submissions/21583?preview=1&rand=350418#

### Wiring
https://www.tinkercad.com/things/4zaOqjpcPmA?sharecode=oPQYZcuKgexSuwHOryOQvVEl419SKq6XD9277Xp_Yus

### Reflection
This assignment was more difficult because I had no clue what any of this code meant at first. But after doing plenty of research and reading people's code I was able to understand what the code is communicating. Otherwise the code itself is quite concise and simple.

## CircuitPyhton_Distance_Sensor

### Description & Code
Create a rainbow gradient with the LED as your your distance sensor reads closer and farther distances.

```python
import time #import files
import board
import neopixel
import adafruit_hcsr04
from adafruit_hcsr04 import HCSR04
import simpleio

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D6, echo_pin=board.D7) #initialize sonar sensor with pins
dot = neopixel.NeoPixel(board.NEOPIXEL, 1) #creates name(dot) for neopixels
dot.brightness =  .1 #sets neopixel brightness

while True:
    try:
        cm = sonar.distance #rewrite sonar distance
        print((cm)) #print sensor distance
        if cm>=5 and cm<=15: #if cm is between 5-15 range colors accordingly
            r=simpleio.map_range(cm,5,15,255,0) #red goes down
            g=simpleio.map_range(cm,5,15,0,0) #green is abscent
            b=simpleio.map_range(cm,5,15,0,255) #blue goes up
            print("Between 5 and 15")
            dot.fill((r,g,b)) #fills led with color
        elif cm>15 and cm<25: #if cm is betwwen 15-25 range colors accordingly
            r=simpleio.map_range(cm,15,25,0,0) #red is abscent
            g=simpleio.map_range(cm,15,25,0,255) #green goes up
            b=simpleio.map_range(cm,15,25,255,0) #blue goes down
            print("Between 15 and 25")
            dot.fill((r,g,b))
        else:  #prints not good if distance is between 5-25
            print("Not Good")
            dot.fill((0,0,0))
    except RuntimeError: #prints retrying if there's an error
        print("Retrying!")
    time.sleep(.01)

```

### Evidence
Another possibly inaccessible video, but this time it's of an LED gradient in accordance to a distance servo.
https://cvilleschools.instructure.com/courses/37129/assignments/493861/submissions/21583?preview=1&rand=336271#

### Wiring
https://www.tinkercad.com/things/6XMrDhjvmKd?sharecode=DWHrZT9ahoq1o2GyyZaeRVFx-oCVnplMcarRY1igdAc

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
