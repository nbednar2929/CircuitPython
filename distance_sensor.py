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