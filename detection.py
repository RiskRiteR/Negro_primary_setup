import cv2 as cv
import numpy as np
from threading import Thread, RLock
from time import sleep


class Detection:
    lock = None
    stopped = True

    rectangles = []
    screenshot = None
    template = None

    def __init__(self):
        self.lock = RLock()

    def find_img(self, threshold=0.97, method=cv.TM_CCORR_NORMED):
        temp_img_w = self.template.shape[1]
        temp_img_h = self.template.shape[0]

        result = cv.matchTemplate(self.screenshot, self.template, method)
        # cv.imshow('SSS', result)
        # cv.waitKey(1)

        locations = np.where(result >= threshold)
        locations = list(zip(*locations[::-1]))

        rectangles = []
        for loc in locations:
            rect = [int(loc[0]), int(loc[1]), temp_img_w, temp_img_h]
            rectangles.append(rect)
            rectangles.append(rect)

        rectangles, weights = cv.groupRectangles(rectangles, groupThreshold=1, eps=0.5)
        return rectangles

    def update_screen(self, screenshot, template):
        self.lock.acquire()
        self.screenshot = screenshot
        self.template = cv.imread(template, cv.IMREAD_UNCHANGED)
        self.lock.release()

    def start(self):
        self.stopped = False
        t = Thread(target=self.run, name='thr_DETECTION', daemon=True)
        t.start()
        print('thr_DETECTION is alive:', t.is_alive())

    def stop(self):
        self.stopped = True

    def run(self):
        while not self.stopped:
            if not self.screenshot is None:
                if not self.template is None:
                    rectangles = self.find_img()
                    if len(rectangles) > 0:
                        self.lock.acquire()
                        self.rectangles = rectangles
                        self.lock.release()
