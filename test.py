import PIL.Image
import cv2 as cv
import numpy as np
import mss
from PIL import Image, ImageGrab
import pyautogui as pag
import win32gui

















while True:
    screen = pag.screenshot(region=(0, 0, 1920, 1080))
    screen = np.array(screen)
    screen = cv.cvtColor(screen, cv.COLOR_RGB2BGR)

    # cv.imshow('Matches', screen)
    # cv.waitKey(10000)
    # exit()
    # screen = cv.imread('1.jpg', cv.IMREAD_UNCHANGED)
    needle_img = cv.imread('2.jpg', cv.IMREAD_UNCHANGED)

    result = cv.matchTemplate(screen, needle_img, cv.TM_CCORR_NORMED)
    # result = find(screen, needle_img)

    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

    print('Best match top left position: %s' % str(max_loc))
    print('Best match confidence: %s' % max_val)

    threshold = 0.95
    if max_val >= threshold:
        print('Found needle.')

        needle_w = needle_img.shape[1]
        needle_h = needle_img.shape[0]

        top_left = max_loc
        bottom_right = (top_left[0] + needle_w, top_left[1] + needle_h)

        cv.rectangle(screen, top_left, bottom_right,
                     color=(0, 255, 0), thickness=2, lineType=cv.LINE_4)

        cv.imshow('Matches', screen)
        cv.imshow('Matchess', result)
        cv.waitKey(1)

    else:
        print('Needle not found.')
