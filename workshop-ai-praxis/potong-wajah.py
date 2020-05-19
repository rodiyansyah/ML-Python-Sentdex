import cv2

detection_model_path = 'haarcascade_files/haarcascade_frontalface_default.xml'
face_detection = cv2.CascadeClassifier(detection_model_path)

cap = cv2.VideoCapture(1)

while(True):
    ret,frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_detection.detectMultiScale(gray)
    if len(faces) > 0:
        for face in faces:
            (fX, fY, fW, fH) = face
            cv2.rectangle(frame, (fX, fY), (fX + fW, fY + fH),
                              (0, 0, 255), 2)


    cv2.imshow("Gambar",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
