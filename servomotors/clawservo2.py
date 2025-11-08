from adafruit_servokit import ServoKit
import time

kit = ServoKit(channels=16)

kit.servo[1].angle = 90
time.sleep(1)

# kit.servo[1].angle = 0
# time.sleep(0.5)

# kit.servo[1].angle = 94
# time.sleep(1)

# kit.servo[1].angle = 0
# time.sleep(0.5)
