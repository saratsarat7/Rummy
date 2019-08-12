import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
from operator import itemgetter
import time

# Test Image
img_rgb = cv.imread('full.png')
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

def find_value(name, rotation):
    # Test Image
    global img_rgb
    global img_gray

    # Symbol
    if (rotation == 0):
        symbol_loc = "images/" + name + ".png"
    else:
        symbol_loc = "joker/" + name + ".png"
    test_symbol = cv.imread(symbol_loc,0)

    # Shape
    w, h = test_symbol.shape[::-1]

    # Matchers
    match_symbol = cv.matchTemplate(img_gray,test_symbol,cv.TM_CCOEFF_NORMED)

    # Accuracy Percentage
    threshold = 0.9

    # Points List
    points = []

    # Selectors
    loc1 = np.where( match_symbol >= threshold)
    for pt in zip(*loc1[::-1]):
        color = list(np.random.choice(range(256), size=3))
        # cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
        cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), color, 2)
        points.append(pt)

    return points

def match_finder(list1, list2):
    for item1 in list1:
        for item2 in list2:
            if ((abs(item1[0]-item2[0]) < 5)):
                if (item2[1] > 350):
                    return (0, item2)
                else:
                    return (1, item2)

def card_finder():
    card_list = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    cart_type = ["diamond", "club", "spade", "heart"]

    dict_points = {}
    for item in (card_list+cart_type):
        dict_points[item] = find_value(item, 0)

    your_hand = []
    common = []
    joker = []

    for type in cart_type:
        for item in card_list:
            result = match_finder(dict_points[type], dict_points[item])
            if (result is not None):
                joker_list = find_value(item, 1)
                if (len(joker) > 0):
                    joker.append((type+item, result[1]))
                
                if (result[0] == 0):
                    your_hand.append((type+item, result[1]))
                else:
                    common.append((type+item, result[1]))

    print(your_hand)
    print(common)
    print(joker)

def process_video():
    global img_rgb
    global img_gray

    cap = cv.VideoCapture('capture.mp4')

    while(cap.isOpened()):
        ret, img_rgb = cap.read()
        img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)

        card_finder()

        cv.namedWindow("frame", cv.WND_PROP_FULLSCREEN)
        cv.setWindowProperty("frame",cv.WND_PROP_FULLSCREEN,cv.WINDOW_FULLSCREEN)
        cv.imshow('frame',img_rgb)
        if cv.waitKey(0) & 0xFF == ord('q'):
            break

import cProfile
cProfile.run('card_finder()', 'function.profile')
# process_video()
# card_finder()
# cv.namedWindow("Result", cv.WND_PROP_FULLSCREEN)
# cv.setWindowProperty("Result",cv.WND_PROP_FULLSCREEN,cv.WINDOW_FULLSCREEN)
# cv.imshow("Result", img_rgb)
# cv.waitKey(0)