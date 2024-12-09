import cv2
import mediapipe as mp
import time

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

def detect_hands(frame, hands):
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
    return frame, results

def is_cheese_pose(hand_landmarks):
    # Check if the index finger and middle finger are extended
    index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
    middle_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
    index_finger_mcp = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP]
    middle_finger_mcp = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP]
    ring_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP]
    pinky_tip = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP]
    thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]

    # Check if index and middle fingers are extended and other fingers are not
    return (index_finger_tip.y < index_finger_mcp.y and
            middle_finger_tip.y < middle_finger_mcp.y and
            ring_finger_tip.y > hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_MCP].y and
            pinky_tip.y > hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_MCP].y and
            thumb_tip.x < hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_IP].x)

def show_image(image_path):
    image = cv2.imread(image_path)
    with mp_hands.Hands(static_image_mode=True, max_num_hands=2, min_detection_confidence=0.5) as hands:
        image, _ = detect_hands(image, hands)
    cv2.imshow("Hand Detection", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def show_video(video_path):
    cap = cv2.VideoCapture(video_path)
    with mp_hands.Hands(max_num_hands=2, min_detection_confidence=0.5, min_tracking_confidence=0.5) as hands:
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            frame, _ = detect_hands(frame, hands)
            cv2.imshow("Hand Detection", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    cap.release()
    cv2.destroyAllWindows()

def show_live_cam():
    cap = cv2.VideoCapture(0)
    with mp_hands.Hands(max_num_hands=2, min_detection_confidence=0.5, min_tracking_confidence=0.5) as hands:
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            frame, results = detect_hands(frame, hands)
            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    if is_cheese_pose(hand_landmarks):
                        timestamp = int(time.time())
                        cv2.imwrite(f"cheese_pose_{timestamp}.png", frame)
                        print(f"Photo taken: cheese_pose_{timestamp}.png")
            cv2.imshow("Hand Detection", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    cap.release()
    cv2.destroyAllWindows()

def main():
    mode = input("Enter 'image' to load from image, 'video' to load from video, or 'live' to use live camera: ").strip().lower()
    if mode == 'image':
        path = input("Enter the path to the image file: ").strip()
        show_image(path)
    elif mode == 'video':
        path = input("Enter the path to the video file: ").strip()
        show_video(path)
    elif mode == 'live':
        show_live_cam()
    else:
        print("Invalid mode selected. Please enter 'image', 'video', or 'live'.")

if __name__ == "__main__":
    main()