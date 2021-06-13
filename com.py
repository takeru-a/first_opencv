import cv2

capture = cv2.VideoCapture(0)

while(True):
    ret, frame = capture.read()
    winsize = (800, 600)
    frame = cv2.resize(frame, winsize)

    cv2.imshow('title', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()

