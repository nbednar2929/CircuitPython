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
        if cm<5:
            print("Less Than 5")
            dot.fill((255,0,0))
        elif cm>5 and cm<20:
            print("Between 5 and 20")
            dot.fill((0,0,255))
        elif cm>20:
            print("Greater Than 20")
            dot.fill((0,255,0))
        else:
            print("Not Good")
            dot.fill((0,0,0))
    except RuntimeError:
        print("Retrying!")
    time.sleep(.25)