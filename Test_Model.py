import cv2
import pickle
import pyttsx3
from utils import get_face_landmarks

emotions = ['HAPPY', 'SAD', 'SURPRISED']

# Load the trained model
with open('./model', 'rb') as f:
    model = pickle.load(f)

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Open the video file
cap = cv2.VideoCapture('C:/Users/amsjf/PycharmProjects/emotion-recognition-python-scikit-learn-mediapipe/peopleSmile.mp4')

while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        break

    face_landmarks = get_face_landmarks(frame, draw=True, static_image_mode=False)

    output = model.predict([face_landmarks])

    emotion = emotions[int(output[0])]

    cv2.putText(frame,
                emotion,
                (10, frame.shape[0] - 1),
                cv2.FONT_HERSHEY_SIMPLEX,
                3,
                (0, 255, 0),
                5)

    cv2.imshow('frame', frame)

    # Speak when certain emotion is detected
    if emotion == 'HAPPY':
        engine.say("Happy person")
    elif emotion == 'SAD':
        engine.say("Sad person")
    elif emotion == 'SURPRISED':
        engine.say("Surprised person")
    engine.runAndWait()

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
