import cv2
import numpy as np

cap = cv2.VideoCapture(0)

if not cap.isOpened():
        print("Error: Could not open camera.")
        exit()

lower_purple = np.array([295, 45, 100])
upper_purple = np.array([295, 100, 25])


while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read frame.")
        break

    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    purple_mask = cv2.inRange(hsv_frame, lower_purple, upper_purple)

    purple_detection = cv2.bitwise_and(frame, frame, mask=purple_mask)

    cv2.imshow("Original Frame", frame)
    cv2.imshow("Purple Detection", purple_detection)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()