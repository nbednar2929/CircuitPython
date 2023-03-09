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

btn = DigitalInOut(board.D13) #create button 
btn.direction = Direction.INPUT #identify button  direction
btn.pull = Pull.DOWN #pull up button 



while True:
    print('Switch1')
    time.sleep(0.1)
    if btn.value: #if button being pressed
        print('Button')
        for angle in range(0, 180, 5):  # 0 - 180 degrees, 5 degrees at a time forward.
            my_servo.angle = angle
            print(angle)
        for angle in range(180, 0, -5):  # 0 - 180 degrees, 5 degrees at a time forward.
            my_servo.angle = angle
