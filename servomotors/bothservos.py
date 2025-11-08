
from adafruit_servokit import ServoKit
import time

kit = ServoKit(channels=16)


kit.continuous_servo[4].throttle = 1
print("Throttle on")

kit.servo[1].angle = 90
time.sleep(1)

kit.servo[1].angle = 0
time.sleep(0.5)

kit.servo[1].angle = 180
time.sleep(1)

kit.servo[1].angle = 0
time.sleep(0.5)

time.sleep(1)
kit.continuous_servo[4].throttle = 0.1
print("sleep")
