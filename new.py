import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# Test Image
img_rgb = cv.imread('test.png')
img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)

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

def find_value(name):
    # Test Image
    global img_rgb
    global img_gray

    # Symbol
    symbol_loc = "images/" + name + ".png"
    test_symbol = cv.imread(symbol_loc,0)

    # Shape
    w, h = test_symbol.shape[::-1]

    # Matchers
    match_symbol = cv.matchTemplate(img_gray,test_symbol,cv.TM_CCOEFF_NORMED)

    # Accuracy Percentage
    threshold = 0.9

    # Selectors
    loc1 = np.where( match_symbol >= threshold)
    for pt in zip(*loc1[::-1]):
        cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
        print(pt)

    cv.imshow('Result', img_rgb)
    cv.waitKey(0)

find_value("K")