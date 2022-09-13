#Nick Bednar
#9/13/22
#Servo shifts between 0-180 degrees back and forth.
import time
import board
import pwmio
from adafruit_motor import servo

# create a PWMOut object on Pin 9.
pwm = pwmio.PWMOut(board.D9, duty_cycle=2 ** 20, frequency=40)

# Create a servo object, my_servo.
my_servo = servo.Servo(pwm)

while True:
    for angle in range(0, 180, 5):  # 0 - 180 degrees, 5 degrees at a time forward.
        my_servo.angle = angle
        time.sleep(0.05)
    for angle in range(180, 0, -5): # 180 - 0 degrees, 5 degrees at a time backward.
        my_servo.angle = angle
        time.sleep(0.05)
