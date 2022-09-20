import time #import files
import board
import neopixel

pixel_pin = board.NEOPIXEL #selects neopixel pin

num_pixels = 1 #number of neopixels

ORDER = neopixel.GRB #reverses rgb order

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER #sets parameters for pixels
)


def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos * 3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos * 3)
        g = 0
        b = int(pos * 3)
    else:
        pos -= 170
        r = 0
        g = int(pos * 3)
        b = int(255 - pos * 3)
    return (r, g, b) if ORDER in (neopixel.RGB, neopixel.GRB) else (r, g, b, 0)


def rainbow_cycle(wait): #colors range in the rainbow
    for j in range(255):
        for i in range(num_pixels):
            pixel_index = (i * 256 // num_pixels) + j
            pixels[i] = wheel(pixel_index & 255)
        pixels.show()
        time.sleep(wait)


while True: #fills pixels with colors
    pixels.fill((255, 0, 0))
    pixels.show()
    time.sleep(1)

    pixels.fill((0, 255, 0))

    pixels.show()
    time.sleep(1)

    pixels.fill((0, 0, 255))
    pixels.show()
    time.sleep(1)

    rainbow_cycle(0.001)  # rainbow cycle with 1ms delay per step