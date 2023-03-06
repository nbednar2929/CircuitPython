import time #importing files
import board
import digitalio
import pwmio
from adafruit_motor import servo
from digitalio import DigitalInOut,Direction,Pull
import simpleio

# create a PWMOut object on Pin 9.
pwm = pwmio.PWMOut(board.D10, duty_cycle=2 ** 20, frequency=40)

# Create a servo object, my_servo.
my_servo = servo.Servo(pwm)

btn = DigitalInOut(board.D8) #create button 
btn.direction = Direction.INPUT #identify button  direction
btn.pull = Pull.UP #pull up button 

switch = DigitalInOut(board.D12) #create switch
switch.direction = Direction.INPUT #identify button direciton

while True:
    if True: #switch.value: #if switch is on
        print('Switch1')
        time.sleep(0.5)
        if btn.value: #if button being pressed
            print('Button')
            for angle in range(0, 180, 5):  # 0 - 180 degrees, 5 degrees at a time forward.
                my_servo.angle = angle
                time.sleep(0.05)
                print(angle)