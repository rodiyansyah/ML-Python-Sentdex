import imutils
import cv2
from keras.models import load_model
from keras.preprocessing.image import img_to_array
import numpy as np

detection_model_path = 'haarcascade_files/haarcascade_frontalface_default.xml'
emotion_model_path = 'models/_mini_XCEPTION.DataBaru.hdf5'

face_detection = cv2.CascadeClassifier(detection_model_path)
emotion_classifier = load_model(emotion_model_path, compile=False)

EMOTIONS = ["marah" ,"jijik","takut","gembira","susah","tercengang","netral"]

cap = cv2.VideoCapture(0)

while(True):
    ret,frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_detection.detectMultiScale(gray)
    if len(faces) > 0:
        for face in faces:
            (fX, fY, fW, fH) = face
            roi = gray[fY:fY + fH, fX:fX + fW]
            roi = cv2.resize(roi, (48, 48))
            roi = roi.astype("float") / 255.0
            roi = img_to_array(roi)
            roi = np.expand_dims(roi, axis=0)

            preds = emotion_classifier.predict(roi)[0]
            emotion_probability = np.max(preds)
            label = EMOTIONS[preds.argmax()]

            cv2.putText(frame,label,(fX,fY-4),
                    cv2.FONT_HERSHEY_SIMPLEX,1,(0, 0, 255))
            cv2.rectangle(frame, (fX, fY), (fX + fW, fY + fH),
                              (0, 0, 255), 2)


    cv2.imshow("Gambar",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
