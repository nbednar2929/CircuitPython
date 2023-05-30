import time #imports
import rotaryio
import board
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
from digitalio import DigitalInOut, Direction, Pull

i2c = board.I2C()
lcd = LCD(I2CPCF8574Interface(i2c, 0x27), num_rows=2, num_cols=16) #identify LCD screen

photoint = DigitalInOut(board.D7) #identify photointerrupter
photoint.pull =Pull.UP #pull up photointerrupter
counter = 0 #create counter set to zero

while True:
    if photoint.value == True: #if photointerrupter 
        counter = counter + 1 #add to counter
        lcd.clear()
        lcd.color = [0, 100, 0]
        lcd.set_cursor_pos(0, 0) #set lcd cursor position
        lcd.print("Interrupts:" + str(counter)) #print interrupts and counter on lcd
        time.sleep(.5) #0.5sec delay
        
