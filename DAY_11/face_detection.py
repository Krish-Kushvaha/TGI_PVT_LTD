import cv2

detector = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

camera = cv2.VideoCapture(0)

print("Webcam Face Detection Started... Press 'q' to Exit")

while True:
    success, image = camera.read()

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    detected_faces = detector.detectMultiScale(
        gray_image,
        scaleFactor=1.1,
        minNeighbors=4
    )

    for (x, y, width, height) in detected_faces:

        cv2.rectangle(
            image,
            (x, y),
            (x + width, y + height),
            (0, 255, 0),
            2
        )

        cv2.putText(
            image,
            "Human Face",
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 0),
            2
        )

    cv2.imshow("Live Face Detector", image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()