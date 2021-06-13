import cv2
import numpy as np

def mosaic(img, alpha):
    w = img.shape[1]
    h = img.shape[0]

    img = cv2.resize(img, (int(w*alpha), int(h*alpha)))
    img = cv2.resize(img,(w, h), interpolation=cv2.INTER_NEAREST)

    return img

cascade = cv2.CascadeClassifier(
    "C:\github\opencv-master\opencv-master\data\haarcascades/haarcascade_frontalface_default.xml"
)

cap = cv2.VideoCapture(0)

while(cap.isOpened()):
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    face = cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3, minSize=(30, 30))

    for (x, y, w, h) in face:
        frame[y:y+h, x:x+w] = mosaic(frame[y:y+h, x:x+w], 0.05)

    cv2.imshow("Flame", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()