import board
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
import time
from digitalio import DigitalInOut, Direction, Pull
from analogio import AnalogIn
import simpleio

i2c = board.I2C() # get and i2c object
lcd = LCD(I2CPCF8574Interface(i2c, 0x27), num_rows=2, num_cols=16)
ptmr = AnalogIn(board.A1)

btn = DigitalInOut(board.D7)
btn.direction = Direction.INPUT
btn.pull = Pull.UP
counter = 0

while True:
    print(ptmr.value)
    if ptmr.value>47000:
        if not btn.value:
            counter = counter+1
            lcd.set_cursor_pos(0,0)
            lcd.print("BTN State: Up  ")
            lcd.set_cursor_pos(1,0)
            lcd.print(str(counter))
    else:
        counter = counter-1
        lcd.set_cursor_pos(0,0)
        lcd.print("BTN State: Down")
        lcd.set_cursor_pos(1,0)
        lcd.print(str(counter))
            

    time.sleep(0.5)