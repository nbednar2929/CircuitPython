import board
import neopixel
import time
import random 

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)
dot.brightness =  .1

print("Make it red!")

r = random.randint(0,255)
g = random.randint(0,255)
b = random.randint(0,255)
rgb = [r,g,b]

if (r>200):
    g + b < 80

if (g>200):
    r + b < 80

if (b>200):
    g + r < 80

while True:
    dot.fill((rgb))
    time.sleep(.5)
    dot.fill((0,0,0))
    time.sleep(0.5)
