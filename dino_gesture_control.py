import cv2
import mediapipe as mp
import pyautogui


# Initialize webcam
def init_camera():
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH,600)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT,500)
    return cap


# Handle space press simulation
def handle_space_press(avg_finger_y, prev_y, threshold):
    if prev_y is not None and abs(avg_finger_y - prev_y) > threshold:
        print("Space pressed")  # Debugging
        pyautogui.press("space")  # Simulate space key press
    return avg_finger_y


def main():
    cap = init_camera()

    # Initialize MediaPipe Hands
    mp_drawing = mp.solutions.drawing_utils
    mp_hands = mp.solutions.hands
    hand = mp_hands.Hands(static_image_mode=False, max_num_hands=1,
                          min_detection_confidence=0.5, min_tracking_confidence=0.5)

    prev_y = None  # Stores previous Y-coordinate of average of fingers
    threshold = 30  # Adjust threshold for movement sensitivity

    # Create a window and set it to always stay on top
    cv2.namedWindow("Hand Tracking", cv2.WINDOW_NORMAL)
    cv2.setWindowProperty("Hand Tracking", cv2.WND_PROP_TOPMOST, 1)

    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            print("Failed to capture frame")
            break

        # Flip the frame for a mirror effect
        frame = cv2.flip(frame, 1)

        # Convert frame to RGB
        RGB_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Process hand landmarks
        result = hand.process(RGB_frame)
        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                # Get Y-coordinates of the 4 fingers (excluding the thumb)
                # Index Finger Tip (Landmark 8)
                index_finger_y = hand_landmarks.landmark[8].y * frame.shape[0]
                # Middle Finger Tip (Landmark 12)
                middle_finger_y = hand_landmarks.landmark[12].y * frame.shape[0]
                # Ring Finger Tip (Landmark 16)
                ring_finger_y = hand_landmarks.landmark[16].y * frame.shape[0]
                # Pinky Finger Tip (Landmark 20)
                pinky_finger_y = hand_landmarks.landmark[20].y * frame.shape[0]

                # Calculate average Y-coordinate of the four fingers
                avg_finger_y = (index_finger_y + middle_finger_y + ring_finger_y + pinky_finger_y) / 4

                # Check for significant movement and simulate space press
                prev_y = handle_space_press(avg_finger_y, prev_y, threshold)

        # Resize the frame
        frame = cv2.resize(frame, (450, 375))
        # Show the output frame
        cv2.imshow("Hand Tracking", frame)

        # Exit when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release resources
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
