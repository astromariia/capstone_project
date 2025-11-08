from adafruit_servokit import ServoKit
import time

kit = ServoKit(channels=16)

kit.continuous_servo[4].throttle = 1
print("Throttle on")
time.sleep(5)
kit.continuous_servo[4].throttle = 0.1
print("sleep")
