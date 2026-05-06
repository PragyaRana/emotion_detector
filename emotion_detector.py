import cv2
from deepface import DeepFace

# Open webcam
cap = cv2.VideoCapture(0)

print("Emotion Detector Started. Press 'q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    try:
        # Analyze emotion
        result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
        emotion = result[0]['dominant_emotion']

        # Draw text on frame
        cv2.putText(frame, f"Emotion: {emotion}", (30, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 3)

    except Exception as e:
        cv2.putText(frame, "No face detected", (30, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.imshow("AI Emotion Detector", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
