import threading
import pyautogui as pag
from pprint import pprint
import os
import cv2 as cv
import numpy as np
from time import time, sleep
from win_cap_detect import WindowCapture
from vision import Vision
from threading import Thread
from logic import LogicPositioning, LogicState


# WindowCapture.list_window_names()
# print(pag.position())
# exit()

DEBUG = True
eve_window = WindowCapture('EVE - Mantori Shaishi')



vision = Vision()
logic = LogicPositioning()

eve_window.start()

logic.start()
detector.update_temp('templates/exiting_dock.jpg')

# loop_time = time()
while True:

    if eve_window.screenshot is None:
        continue

    detector.update(eve_window.screenshot)
    logic.update_win_cap(eve_window.window_rect)

    if logic.state == LogicState.INITIALIZING:
        while True:
            targets = vision.get_click_for_chat(detector.rectangles)
            logic.update_targets(targets)
            if logic.state == LogicState.DOCK:
                break

    elif logic.state == LogicState.DOCK:
        detector.update_temp('templates/chat_local.jpg')
        while True:
            targets = vision.get_click_for_chat(detector.rectangles)
            logic.update_targets(targets)
            if logic.state == LogicState.CUSTOM_CHAT:
                break

    elif logic.state == LogicState.CUSTOM_CHAT:
        pass

    elif logic.state == LogicState.SCAN_NEOCOM:
        detector.update_temp('templates/neocom.jpg')
        while True:
            targets = vision.get_click_for_neocom(detector.rectangles)
            logic.update_targets(targets)
            if logic.state == LogicState.CUSTOM_NEOCOM:
                break

    elif logic.state == LogicState.CUSTOM_NEOCOM:
        pass

    elif logic.state == LogicState.SCAN_LOCK_NEOCOM:
        detector.update_temp('templates/lock_neocom.jpg')
        while True:
            targets = vision.get_click_center(detector.rectangles)
            logic.update_targets(targets)
            if logic.state == LogicState.LOCK_NEOCOM:
                break

    elif logic.state == LogicState.LOCK_NEOCOM:
        pass

    elif logic.state == LogicState.SCAN_UNNECESSARY_MENU:
        detector.update_temp('templates/unnecessary_menu.jpg')
        while True:
            targets = vision.get_click_center(detector.rectangles)
            logic.update_targets(targets)
            if logic.state == LogicState.LOCK_NEOCOM:
                break

    elif logic.state == LogicState.LOCK_UNNECESSARY_MENU:
        pass

    if DEBUG:
        debug_image = vision.draw_rectangles(eve_window.screenshot, detector.rectangles)
        cv.imshow('Window', debug_image)

    # print('FPS {}'.format(1 / (time() - loop_time)))
    # loop_time = time()

    key = cv.waitKey(1000)
    if key == ord("q"):
        eve_window.stop()
        detector.stop()
        cv.destroyAllWindows()
        logic.stop()
        break

print("[INFO] Done.")
