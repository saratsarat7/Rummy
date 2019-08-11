import cv2
import numpy as np
import time

def test(img):
    cv2.imshow('Image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    exit()

img = cv2.imread('test.png',1)

#--- create a blank image of the same size for storing the green rectangles (boundaries) ---
black = np.zeros_like(img)
img2 = np.zeros_like(img)

#--- convert your image to grayscale and apply a threshold ---
gray1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
# ret2, th2 = cv2.threshold(gray1, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

th = cv2.adaptiveThreshold(gray1,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,11,2)

#--- perform morphological operation to ensure smaller portions are part of a single character ---
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
threshed = cv2.morphologyEx(th, cv2.MORPH_CLOSE, kernel)

#--- find contours ---
# imgContours, Contours, Hierarchy = cv2.findContours(threshed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
Contours, Hierarchy = cv2.findContours(threshed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
for contour in Contours:

    #--- select contours above a certain area ---
    if cv2.contourArea(contour) > 200:

        #--- store the coordinates of the bounding boxes ---
        [X, Y, W, H] = cv2.boundingRect(contour)

        #--- draw those bounding boxes in the actual image as well as the plain blank image ---
        cv2.rectangle(img2, (X, Y), (X + W, Y + H), (0,0,255), 2)
        cv2.rectangle(black, (X, Y), (X + W, Y + H), (0,255,0), 2)

cv2.imshow('contour', img2)
cv2.imshow('black', black)
cv2.waitKey(0)