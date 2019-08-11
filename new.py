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
    width = int(image.shape[1] / 15)
    height = int(image.shape[0] / 15)
    dim = (width, height)
    image = cv.resize(image, dim, interpolation = cv.INTER_AREA)
    return image

# Symbols
spade = cv.imread('images/spade.png',0)
diamond = cv.imread('images/diamond.png',0)
club = cv.imread('images/club.png',0)
heart = cv.imread('images/heart.png',0)

# Numbers
eight = cv.imread('images/8.png',0)

# Shapes
w1, h1 = spade.shape[::-1]
w2, h2 = diamond.shape[::-1]
w3, h3 = club.shape[::-1]
w4, h4 = heart.shape[::-1]

# Test Image
img_rgb = cv.imread('test.png')
img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)

# Matchers
match_spade = cv.matchTemplate(img_gray,spade,cv.TM_CCOEFF_NORMED)
_, confidence, _, _ = cv.minMaxLoc(match_spade)
print("Space Confidence : "+str(confidence))

match_diamond = cv.matchTemplate(img_gray,diamond,cv.TM_CCOEFF_NORMED)
_, confidence, _, _ = cv.minMaxLoc(match_diamond)
print("Diamond Confidence : "+str(confidence))

match_club = cv.matchTemplate(img_gray,club,cv.TM_CCOEFF_NORMED)
_, confidence, _, _ = cv.minMaxLoc(match_club)
print("Club Confidence : "+str(confidence))

match_heart = cv.matchTemplate(img_gray,heart,cv.TM_CCOEFF_NORMED)
_, confidence, _, _ = cv.minMaxLoc(match_heart)
print("Heart Confidence : "+str(confidence))

# Accuracy Percentage
threshold = 0.95

# Selectors
loc1 = np.where( match_spade >= threshold)
for pt in zip(*loc1[::-1]):
    cv.rectangle(img_rgb, pt, (pt[0] + w1, pt[1] + h1), (0,0,255), 2)

loc2 = np.where( match_diamond >= threshold)
for pt in zip(*loc2[::-1]):
    cv.rectangle(img_rgb, pt, (pt[0] + w2, pt[1] + h2), (0,255,0), 2)

loc3 = np.where( match_club >= threshold)
for pt in zip(*loc3[::-1]):
    cv.rectangle(img_rgb, pt, (pt[0] + w3, pt[1] + h3), (255,0,0), 2)

loc4 = np.where( match_heart >= threshold)
for pt in zip(*loc4[::-1]):
    cv.rectangle(img_rgb, pt, (pt[0] + w4, pt[1] + h4), (100,100,100), 2)

cv.imshow('Result', img_rgb)
cv.waitKey(0)