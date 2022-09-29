import time #importing files
import board
import pwmio
from adafruit_motor import servo
from digitalio import DigitalInOut,Direction,Pull
import simpleio

# create a PWMOut object on Pin 9.
pwm = pwmio.PWMOut(board.D7, duty_cycle=2 ** 20, frequency=40)

# Create a servo object, my_servo.
my_servo = servo.Servo(pwm)

btn = DigitalInOut(board.D4) #create button 1
btn2 = DigitalInOut(board.D3) #create button 2
btn.direction = Direction.INPUT #create button 1 direction
btn.pull = Pull.UP #pull up button 1
btn2.direction = Direction.INPUT #create button 2 direction
btn2.pull = Pull.UP #pull up button 2

while True:
    if not btn.value: #button 1 being pressed
        for angle in range(0, 180, 5):  # 0 - 180 degrees, 5 degrees at a time forward.
            my_servo.angle = angle
            time.sleep(0.05)
    if not btn2.value: #button 2 being pressed
        for angle in range(180, 0, -5): # 180 - 0 degrees, 5 degrees at a time backward.
            my_servo.angle = angle
            time.sleep(0.05)