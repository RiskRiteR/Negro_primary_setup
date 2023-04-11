import numpy as np
import win32gui
import mss
from threading import Thread, Lock
import cv2 as cv
from time import sleep


class WindowCapture:
    window_handle = None
    stopped = True
    lock = None
    screenshot = None
    rectangles = []
    template = None
    method = None

    w = 0
    h = 0
    threshold = 0
    border_pixels = 11
    titlebar_pixels = 45
    window_rect = (0, 0, 0, 0)
    temp_img_w = 0
    temp_img_h = 0

    def __init__(self, window_name=None, threshold=0.97, method=cv.TM_CCORR_NORMED):
        self.lock = Lock()
        if window_name is None:
            self.window_handle = win32gui.GetDesktopWindow()
        else:
            self.window_handle = win32gui.FindWindow(None, window_name)
            win32gui.SetForegroundWindow(win32gui.FindWindow(None, window_name))
            self.threshold = threshold
            self.method = method

    def get_position_window(self):
        self.window_rect = win32gui.GetWindowRect(self.window_handle)
        x_left, y_up, x_right, y_down = self.window_rect
        self.w = x_right - x_left
        self.h = y_down - y_up
        self.w = self.w - (self.border_pixels * 2)
        self.h = self.h - self.titlebar_pixels - self.border_pixels
        return self.window_rect, self.w, self.h

    def get_screenshot(self):
        with mss.mss() as stc:
            monitor = {
                'left': self.window_rect[0] + self.border_pixels,
                'top': self.window_rect[1] + self.titlebar_pixels,
                'width': self.w,
                'height': self.h
            }

        img = np.array(stc.grab(monitor))
        img = img[..., :3]
        img = np.ascontiguousarray(img)

        return img

    # def find_img(self):
    #     self.temp_img_w = self.template.shape[1]
    #     self.temp_img_h = self.template.shape[0]
    #
    #     result = cv.matchTemplate(self.get_screenshot(), self.template, self.method)
    #     # cv.imshow('SSS', result)
    #     # cv.waitKey(1)
    #
    #     locations = np.where(result >= self.threshold)
    #     locations = list(zip(*locations[::-1]))
    #
    #     rectangles = []
    #     for loc in locations:
    #         rect = [int(loc[0]), int(loc[1]), self.temp_img_w, self.temp_img_h]
    #         rectangles.append(rect)
    #         rectangles.append(rect)
    #
    #     rectangles, weights = cv.groupRectangles(rectangles, groupThreshold=1, eps=0.5)
    #     return rectangles

    @staticmethod
    def list_window_names():
        def win_enum_handler(hwnd, ctx):
            if win32gui.IsWindowVisible(hwnd):
                print(hex(hwnd), win32gui.GetWindowText(hwnd))
        win32gui.EnumWindows(win_enum_handler, None)

    def start(self):
        self.stopped = False
        t = Thread(target=self.run)
        t.start()

    # def update(self, screenshot):
    #     self.lock.acquire()
    #     self.screenshot = screenshot
    #     self.lock.release()

    # def update_temp(self, templates):
    #     template = cv.imread(templates, cv.IMREAD_UNCHANGED)
    #     self.lock.acquire()
    #     self.template = template
    #     self.lock.release()

    def stop(self):
        self.stopped = True

    def run(self):
        while not self.stopped:
            if len(self.rectangles) == 0:
                self.window_rect, self.w, self.h = self.get_position_window()
                screenshot = self.get_screenshot()
                self.lock.acquire()
                self.screenshot = screenshot
                self.lock.release()
                # if not self.screenshot is None:
                #     rectangles = self.find_img()
                #     self.lock.acquire()
                #     self.rectangles = rectangles
                #     self.lock.release()
