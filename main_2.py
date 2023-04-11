import threading
import multiprocessing
import pyautogui as pag
from pprint import pprint
import os
import cv2 as cv
import numpy as np
from time import time, sleep
from win_capture import WindowCapture
from detection import Detection
from vision import Vision
from threading import Thread
from logic_2 import LogicPositioning, LogicState


if __name__ == '__main__':

    # WindowCapture.list_window_names()
    # print(pag.position())
    # exit()

    DEBUG = True

    # queue = multiprocessing.Queue(maxsize=1)
    eve_window = WindowCapture('EVE - Mantori Shaishi')
    detector = Detection()
    vision = Vision()
    logic = LogicPositioning()

    # main_thread = threading.main_thread()
    # main_process = multiprocessing.parent_process()

    eve_window.start()
    detector.start()
    logic.start()

    # for t in threading.enumerate():
    #     print(t)
    #     if t is main_thread:
    #         continue
    #     print(f'Ожидание выполнения потока {t.name}')
    #     t.join()

    print('activ thread:', threading.active_count())
    print('enumerate:', threading.enumerate())
    print('activ process:', multiprocessing.active_children())
    # print('enumerate:', multiprocessing.parent_process())



    # loop_time = time()
    while True:

        if eve_window.screenshot is None:
            continue

        detector.update_screen(eve_window.screenshot, 'templates/exiting_dock.jpg')


        if logic.state == LogicState.INITIALIZING:
            targets = vision.get_click_for_chat(detector.rectangles)



        if DEBUG:
            debug_image = vision.draw_rectangles(eve_window.screenshot, detector.rectangles)
            cv.imshow('Window', debug_image)

        # print('FPS {}'.format(1 / (time() - loop_time)))
        # loop_time = time()

        key = cv.waitKey(1)
        if key == ord("q"):
            cv.destroyAllWindows()
            break

    print("[INFO] Done.")
