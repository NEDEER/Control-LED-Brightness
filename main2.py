import pyfirmata2
import mediapipe as mp
import math
import cv2
import time

board = pyfirmata2.Arduino("COM10")
ledPin = board.get_pin("d:3:p")

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 600)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 500)

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
hand = mp_hands.Hands(max_num_hands=1)

while True:
    success, frame = cap.read()
    if success:
        RGB_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hand.process(RGB_frame)
        if result.multi_hand_landmarks:
            handLandmarks = result.multi_hand_landmarks[0]
            thumbTip = handLandmarks.landmark[4]
            indexTip = handLandmarks.landmark[8]

            # Get the coordinates of the landmarks
            thumb_x = int(thumbTip.x * frame.shape[1])
            thumb_y = int(thumbTip.y * frame.shape[0])
            index_x = int(indexTip.x * frame.shape[1])
            index_y = int(indexTip.y * frame.shape[0])

            # Calculate the distance
            distance = math.sqrt((thumb_x - index_x)**2 + (thumb_y - index_y)**2)

            # Display the distance on the frame
            cv2.putText(frame, f"Distance: {int(distance)}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            # Draw the landmarks and connections on the frame
            mp_drawing.draw_landmarks(frame, handLandmarks, mp_hands.HAND_CONNECTIONS)

            # Scale distance for LED control (optional, depends on the LED behavior)
            led_value = min(distance / 100, 1)
            ledPin.write(led_value)

        cv2.imshow("capture image", frame)
        if cv2.waitKey(1) == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
