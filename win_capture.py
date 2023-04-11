import numpy as np
import win32gui
import mss
import cv2 as cv
from time import sleep
from threading import Thread, RLock
import multiprocessing


class WindowCapture:
    lock = None
    stopped = True
    mlock = None

    screenshot = None
    window_handle = None

    w = 0
    h = 0
    border_pixels = 11
    titlebar_pixels = 45
    window_rect = (0, 0, 0, 0)
    temp_img_w = 0
    temp_img_h = 0

    def __init__(self, window_name=None):
        self.lock = RLock()
        if window_name is None:
            self.window_handle = win32gui.GetDesktopWindow()
        else:
            self.window_handle = win32gui.FindWindow(None, window_name)
            win32gui.SetForegroundWindow(win32gui.FindWindow(None, window_name))

    def get_position_window(self):
        self.window_rect = win32gui.GetWindowRect(self.window_handle)
        x_left, y_up, x_right, y_down = self.window_rect
        self.w = x_right - x_left
        self.h = y_down - y_up
        self.w = self.w - (self.border_pixels * 2)
        self.h = self.h - self.titlebar_pixels - self.border_pixels
        return list((self.window_rect, self.w, self.h))

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

    @staticmethod
    def list_window_names():
        def win_enum_handler(hwnd, ctx):
            if win32gui.IsWindowVisible(hwnd):
                print(hex(hwnd), win32gui.GetWindowText(hwnd))
        win32gui.EnumWindows(win_enum_handler, None)

    def get_coordinates(self, queue):
        queue.put('text')

    def start(self):
        self.stopped = False
        t = Thread(target=self.run, name='thr_WIN_CAPTURE', daemon=True)
        t.start()
        print('thr_WIN_CAPTURE is alive:', t.is_alive())

    def stop(self):
        self.stopped = True

    def run(self):
        while not self.stopped:
            window_rect, w, h = self.get_position_window()
            screenshot = self.get_screenshot()
            self.lock.acquire()
            self.window_rect, self.w, self.h = window_rect, w, h
            self.screenshot = screenshot
            self.lock.release()
