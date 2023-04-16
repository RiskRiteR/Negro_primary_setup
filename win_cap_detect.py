import mss
import asyncio
import win32gui
import cv2 as cv
import numpy as np


class WindowCapture:
    window_handle = None
    screenshot = None
    template = None
    rectangles = []

    w = 0
    h = 0
    border_pixels = 11
    titlebar_pixels = 45
    window_rect = (0, 0, 0, 0)
    temp_img_w = 0
    temp_img_h = 0

    def __init__(self, window_name=None):
        if window_name is None:
            self.window_handle = win32gui.GetDesktopWindow()
        else:
            self.window_handle = win32gui.FindWindow(None, window_name)
            win32gui.SetForegroundWindow(win32gui.FindWindow(None, window_name))

    async def get_position_window(self):
        self.window_rect = win32gui.GetWindowRect(self.window_handle)
        x_left, y_up, x_right, y_down = self.window_rect
        self.w = x_right - x_left
        self.h = y_down - y_up
        self.w = self.w - (self.border_pixels * 2)
        self.h = self.h - self.titlebar_pixels - self.border_pixels
        return self.window_rect, self.w, self.h

    async def get_screenshot(self):
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
        self.screenshot = img
        return None

    async def find_img(self, threshold=0.97, method=cv.TM_CCORR_NORMED):
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

        self.rectangles, weights = cv.groupRectangles(rectangles, groupThreshold=1, eps=0.5)
        return None

    def update_template(self, template):
        self.template = cv.imread(template, cv.IMREAD_UNCHANGED)
        return None

    @staticmethod
    def list_window_names():
        def win_enum_handler(hwnd, ctx):
            if win32gui.IsWindowVisible(hwnd):
                print(hex(hwnd), win32gui.GetWindowText(hwnd))
        win32gui.EnumWindows(win_enum_handler, None)

    async def main(self):
        task_1 = asyncio.create_task(self.get_position_window())
        task_2 = asyncio.create_task(self.get_screenshot())
        task_3 = asyncio.create_task(self.find_img())
