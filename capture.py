import numpy as np
import cv2 as cv

cap = cv.VideoCapture('capture.mp4')

while(cap.isOpened()):
    ret, frame = cap.read()

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    cv.namedWindow("frame", cv.WND_PROP_FULLSCREEN)
    cv.setWindowProperty("frame",cv.WND_PROP_FULLSCREEN,cv.WINDOW_FULLSCREEN)
    cv.imshow('frame',gray)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()