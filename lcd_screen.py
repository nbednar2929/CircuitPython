import board
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
import time
from digitalio import DigitalInOut, Direction, Pull
from analogio import AnalogIn
import simpleio

i2c = board.I2C() #get an i2c object
lcd = LCD(I2CPCF8574Interface(i2c, 0x27), num_rows=2, num_cols=16)
ptmr = AnalogIn(board.A1)

btn = DigitalInOut(board.D7)
btn.direction = Direction.INPUT
btn.pull = Pull.UP
counter = 0


while True:
    print(ptmr.value)
    if ptmr.value<47000 and not btn.value:
        lcd.set_cursor_pos(0,0)
        lcd.print("BTN State: Down  ")
        lcd.set_cursor_pos(1,0)
        lcd.print('Presses:')
        lcd.set_cursor_pos(1,12)
        lcd.print(str(counter))
        counter = counter-1            
    else:
        lcd.set_cursor_pos(0,0)
        lcd.print("BTN State: Up   ")
        lcd.set_cursor_pos(1,0)
        lcd.print('Presses:')
        lcd.set_cursor_pos(1,12)
        lcd.print(str(counter))
        counter = counter+1

    time.sleep(0.5)
#problems: counts without button press
#zeros stay on the lcd when counting back from ten