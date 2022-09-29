import board #imoprt all files
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
import time
from digitalio import DigitalInOut, Direction, Pull
from analogio import AnalogIn
import simpleio

i2c = board.I2C() #get an i2c object 
lcd = LCD(I2CPCF8574Interface(i2c, 0x27), num_rows=2, num_cols=16) #initiate LCD screen
ptmr = AnalogIn(board.A1) #identify potentiometer

btn = DigitalInOut(board.D7) #identify button
btn.direction = Direction.INPUT #identify button direction
btn.pull = Pull.UP #pull button up
counter = 0 #initialize counter
delta = 1 #initialize variable that counter changes by
lastBtn = btn.value #creates a second button value variable to call back to

while True:
    print(ptmr.value) #print potentiometer value
    lcd.set_cursor_pos(1,0) #set lcd cursor
    lcd.print(" Presses:") #print presses
    lcd.set_cursor_pos(1,12) #set lcd cursor
    lcd.print(str(counter)) #print counter
    lcd.print(" ") #removes excess integers after going between 9-11
   
    
    if ptmr.value<47000: #if potentiometer reads less than 47,000
        lcd.set_cursor_pos(0,0) #set cursor on lcd
        lcd.print("BTN State: Down  ") #print button state: down
        delta = -1 #set delta to -1
    else:
        lcd.set_cursor_pos(0,0) #set lcd cursor
        lcd.print("BTN State: UP    ") #print button state up
        delta = 1 #set delta to 1
    
    if not btn.value and lastBtn != btn.value: #if button is being pressed and button value is not the same as it was prior
        counter = counter + delta #add delta to counter

    lastBtn = btn.value #restating lastBtn
    time.sleep(0.05)
#problems: counts without button press
#zeros stay on the lcd when counting back from ten