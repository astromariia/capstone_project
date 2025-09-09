motor1 = Motor(forward=17, backward=18)

print("Moving motors forward...")
motor1.forward()
sleep(2)

print("Moving motors backward at half speed...")
motor1.backward(speed=0.5)
sleep(2)

print("Stopping motors...")
motor1.stop()
sleep(2)

if __name__ == "__main__":
    try:
        control_motors()
    except KeyboardInterrupt:
        print("Program interrupted. Stopping motors.")
        motor1.stop()
