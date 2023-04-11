import multiprocessing
import cv2 as cv
import random
import pyautogui as pag
from time import sleep, time
# from threading import Thread, RLock
from multiprocessing import Process, RLock
from math import sqrt
from mouse_user import MouseUtils


class LogicState:
    INITIALIZING = 0
    DOCK = 1
    CUSTOM_CHAT = 2
    SCAN_NEOCOM = 3
    CUSTOM_NEOCOM = 4
    SCAN_LOCK_NEOCOM = 5
    LOCK_NEOCOM = 6
    SCAN_UNNECESSARY_MENU = 7
    LOCK_UNNECESSARY_MENU = 8
    UNDOCK = 100


class LogicPositioning(Process):
    INITIALIZING_SECONDS = 2

    stopped = False
    lock = None
    state = None
    timestamp = None
    window_position = None

    targets = [(800, 800)]
    border_pixels = 11
    titlebar_pixels = 45

    def __init__(self):
        Process.__init__(self, target=self.run, args=(self.lock,), name='pro_LOGIC', daemon=True)
        self.lock = RLock()
        self.state = LogicState.INITIALIZING
        self.timestamp = time()

    def window_custom_chat(self):
        MouseUtils.move_to(self.get_screen_position(self.targets[0]), 10, 1)
        sleep(random.uniform(0.4, 0.8))

        # pag.mouseDown((pag.position()), button='left')
        # sleep(random.uniform(0.3, 0.7))
        # MouseUtils.move_to((pag.position()[0], pag.position()[1] + 160))
        # sleep(random.uniform(0.6, 1))
        # pag.mouseUp((pag.position()), button='left')
        # sleep(random.uniform(0.8, 1.4))
        return True

    def custom_neocom(self):
        MouseUtils.move_to(self.get_screen_position(self.targets[0]), 5, 1)
        sleep(random.uniform(0.4, 0.8))

        # pag.mouseDown((pag.position()), button='left')
        # sleep(random.uniform(0.2, 0.3))
        # pag.mouseUp((pag.position()), button='left')
        # sleep(random.uniform(0.4, 0.8))
        #
        # pag.keyDown('ctrl')
        # sleep(random.uniform(0.8, 1.2))
        # pag.keyDown('shift')
        # sleep(random.uniform(0.4, 0.8))
        # pag.keyDown('f9')
        # sleep(random.uniform(0.4, 0.7))
        # pag.keyUp('f9')
        # sleep(random.uniform(0.5, 0.9))
        # pag.keyUp('shift')
        # sleep(random.uniform(0.3, 0.6))
        # pag.keyUp('ctrl')

        pag.mouseDown((pag.position()), button='right')
        sleep(random.uniform(0.3, 0.4))
        pag.mouseUp((pag.position()), button='right')
        sleep(random.uniform(0.4, 0.8))
        return True

    def lock_neocom(self):
        MouseUtils.move_to(self.get_screen_position(self.targets[0]), 7, 2)
        sleep(random.uniform(0.4, 0.8))

        # pag.mouseDown((pag.position()), button='left')
        # sleep(random.uniform(0.2, 0.3))
        # pag.mouseUp((pag.position()), button='left')
        # sleep(random.uniform(0.4, 0.8))
        return True

    def lock_unnecessary_menu(self):
        MouseUtils.move_to(self.get_screen_position(self.targets[0]), 2, 2)
        sleep(random.uniform(0.4, 0.8))

        # pag.mouseDown((pag.position()), button='left')
        # sleep(random.uniform(0.2, 0.3))
        # pag.mouseUp((pag.position()), button='left')
        # sleep(random.uniform(0.4, 0.8))
        #
        # pag.keyDown('alt')
        # sleep(random.uniform(0.6, 1.1))
        # pag.keyDown('c')
        # sleep(random.uniform(0.2, 0.5))
        # pag.keyUp('c')
        # sleep(random.uniform(0.3, 0.6))
        # pag.keyUp('alt')
        # sleep(random.uniform(0.4, 0.8))
        return True

    def get_screen_position(self, pos):
        x = pos[0] + self.window_position[0] + self.border_pixels
        y = pos[1] + self.window_position[1] + self.titlebar_pixels
        return x, y

    def run(self):
        while not self.stopped:
            print(self.window_position)
            if not self.window_position is None:
                if len(self.targets) > 0:
                    if self.state == LogicState.INITIALIZING:
                        if time() > self.timestamp + self.INITIALIZING_SECONDS:
                            if len(self.targets) > 0:
                                # print(self.window_position, self.targets)
                                self.lock.acquire()
                                print('INITIALIZING Вошёл')
                                self.state = LogicState.DOCK
                                self.lock.release()
                                print('INITIALIZING Ушёл')
                            else:
                                self.lock.acquire()
                                self.state = LogicState.UNDOCK
                                self.lock.release()

                    elif self.state == LogicState.DOCK:
                        sleep(random.uniform(2.5, 3))
                        if len(self.targets) > 0:
                            self.lock.acquire()
                            print('DOCK Вошёл')
                            self.state = LogicState.CUSTOM_CHAT
                            self.lock.release()
                            print('DOCK Ушёл')
                        else:
                            self.lock.acquire()
                            self.state = LogicState.INITIALIZING
                            self.lock.release()
                            with open('debug.txt', 'a') as file:
                                file.write('not detected templates/chat_local.jpg\n')
                    #
                    # elif self.state == LogicState.CUSTOM_CHAT:
                    #     self.window_custom_chat()
                    #     self.lock.acquire()
                    #     print('CUSTOM_CHAT Вошёл')
                    #     self.state = LogicState.SCAN_NEOCOM
                    #     self.lock.release()
                    #     print('CUSTOM_CHAT Ушёл')
                    #
                    # elif self.state == LogicState.SCAN_NEOCOM:
                    #     sleep(random.uniform(2.5, 3))
                    #     if len(self.targets) > 0:
                    #         self.lock.acquire()
                    #         print('SCAN_NEOCOM Вошёл')
                    #         self.state = LogicState.CUSTOM_NEOCOM
                    #         self.lock.release()
                    #         print('SCAN_NEOCOM Ушёл')
                    #     else:
                    #         self.lock.acquire()
                    #         self.state = LogicState.SCAN_NEOCOM
                    #         self.lock.release()
                    #         with open('debug.txt', 'a') as file:
                    #             file.write('not detected templates/neocom.jpg\n')
                    #
                    # elif self.state == LogicState.CUSTOM_NEOCOM:
                    #     self.custom_neocom()
                    #     self.lock.acquire()
                    #     print('CUSTOM_NEOCOM Вошёл')
                    #     self.state = LogicState.SCAN_LOCK_NEOCOM
                    #     self.lock.release()
                    #     print('CUSTOM_NEOCOM Ушёл')
                    #
                    # elif self.state == LogicState.SCAN_LOCK_NEOCOM:
                    #     sleep(random.uniform(2.5, 3))
                    #     if len(self.targets) > 0:
                    #         self.lock.acquire()
                    #         print('SCAN_LOCK_NEOCOM Вошёл')
                    #         self.state = LogicState.LOCK_NEOCOM
                    #         self.lock.release()
                    #         print('SCAN_LOCK_NEOCOM Ушёл')
                    #     else:
                    #         self.lock.acquire()
                    #         self.state = LogicState.SCAN_LOCK_NEOCOM
                    #         self.lock.release()
                    #         with open('debug.txt', 'a') as file:
                    #             file.write('not detected templates/lock_neocom.jpg\n')
                    #
                    # elif self.state == LogicState.LOCK_NEOCOM:
                    #     self.lock_neocom()
                    #     self.lock.acquire()
                    #     print('LOCK_NEOCOM Вошёл')
                    #     self.state = LogicState.SCAN_UNNECESSARY_MENU
                    #     self.lock.release()
                    #     print('LOCK_NEOCOM Ушёл')
                    #
                    # elif self.state == LogicState.SCAN_UNNECESSARY_MENU:
                    #     sleep(random.uniform(2.5, 3))
                    #     if len(self.targets) > 0:
                    #         self.lock.acquire()
                    #         print('SCAN_UNNECESSARY_MENU Вошёл')
                    #         self.state = LogicState.LOCK_UNNECESSARY_MENU
                    #         self.lock.release()
                    #         print('SCAN_UNNECESSARY_MENU Ушёл')
                    #     else:
                    #         self.lock.acquire()
                    #         self.state = LogicState.SCAN_UNNECESSARY_MENU
                    #         self.lock.release()
                    #         with open('debug.txt', 'a') as file:
                    #             file.write('not detected templates/unnecessary_menu.jpg\n')
                    #
                    # elif self.state == LogicState.LOCK_UNNECESSARY_MENU:
                    #     self.lock_unnecessary_menu()
                    #     self.lock.acquire()
                    #     print('LOCK_UNNECESSARY_MENU Вошёл')
                    #     self.state = LogicState.SCAN_UNNECESSARY_MENU
                    #     self.lock.release()
                    #     print('LOCK_UNNECESSARY_MENU Ушёл')
                    #     self.stopped = True
