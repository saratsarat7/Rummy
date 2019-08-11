import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def image_max(image):
    width = int(image.shape[1] * 5)
    height = int(image.shape[0] * 5)
    dim = (width, height)
    image = cv.resize(image, dim, interpolation = cv.INTER_AREA)
    return image

def image_min(image):
    width = int(image.shape[1] / 5)
    height = int(image.shape[0] / 5)
    dim = (width, height)
    image = cv.resize(image, dim, interpolation = cv.INTER_AREA)
    return image

img_rgb = cv.imread('1.png')
img_rgb = image_max(img_rgb)
img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)

diamond = cv.imread('images/club.png',0)
eight = cv.imread('8.png',0)

w1, h1 = diamond.shape[::-1]
w2, h2 = eight.shape[::-1]

res1 = cv.matchTemplate(img_gray,diamond,cv.TM_CCOEFF_NORMED)
print(res1.shape)
res2 = cv.matchTemplate(img_gray,eight,cv.TM_CCOEFF_NORMED)
print(res2.shape)

threshold = 0.8

# while (1):
#     thresh = 0.8
#     res = cv.matchTemplate(img_gray, diamond, cv.TM_CCOEFF_NORMED)
#     # res = cv.threshold(res, res, 0.8, 1., cv.THRESH_TOZERO)
#     _, confidence, _, _ = cv.minMaxLoc(res)
#     # cv.minMaxLoc(res, minval, &maxval, &minloc, &maxloc);
#     # print(confidence)
#     threshold = confidence
#     if (confidence < thresh):
#         width = int(diamond.shape[1]-1)
#         height = int(diamond.shape[0]-1)
#         dim = (width, height)
#         diamond = cv.resize(diamond, dim, interpolation = cv.INTER_AREA)
#         cv.imshow('Diamond', diamond)
#         cv.waitKey(0)
#     else:
#         break

loc1 = np.where( res1 >= threshold)
for pt in zip(*loc1[::-1]):
    cv.rectangle(img_rgb, pt, (pt[0] + w1, pt[1] + h1), (0,0,255), 2)

loc2 = np.where( res2 >= threshold)
for pt in zip(*loc2[::-1]):
    cv.rectangle(img_rgb, pt, (pt[0] + w2, pt[1] + h2), (0,255,0), 2)

img_rgb = image_min(img_rgb)
cv.imshow('Result', img_rgb)
cv.waitKey(0)