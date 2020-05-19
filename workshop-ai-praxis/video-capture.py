import cv2

cap = cv2.VideoCapture(1)

while(True):
    ret,frame = cap.read()
    print (ret)
    cv2.imshow('Gambar',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
