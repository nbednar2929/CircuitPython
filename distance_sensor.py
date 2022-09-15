import time
import board
import neopixel
import adafruit_hcsr04
from adafruit_hcsr04 import HCSR04
import simpleio

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D6, echo_pin=board.D7)
dot = neopixel.NeoPixel(board.NEOPIXEL, 1) #creates name(dot) for neopixels
dot.brightness =  .1 #sets neopixel brightness

while True:
    try:
        cm = sonar.distance
        print((cm))
        if cm>=5 and cm<=15:
            r=simpleio.map_range(cm,5,15,255,0)
            g=simpleio.map_range(cm,5,15,0,0)
            b=simpleio.map_range(cm,5,15,0,255)
            print("Between 5 and 15")
            dot.fill((r,g,b))
        elif cm>15 and cm<35:
            r=simpleio.map_range(cm,15,50,0,0)
            g=simpleio.map_range(cm,15,50,0,255)
            b=simpleio.map_range(cm,15,50,255,0)
            print("Between 15 and 35")
            dot.fill((r,g,b))
        else:
            print("Not Good")
            dot.fill((0,0,0))
    except RuntimeError:
        print("Retrying!")
    time.sleep(.1)