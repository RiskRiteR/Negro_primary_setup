import asyncio

import random
import pyautogui as pag
from time import sleep, time
from mouse_user import MouseUtils


class LogicState:
    SCAN_START_LAUNCHER = 0
    START_LAUNCHER = 1
    SCAN_START_GAME = 2
    START_GAME = 3
    SCAN_LOCK_LAUNCHER = 4
    LOCK_LAUNCHER = 5
    STOP_LAUNCH = 6

    SCAN_DETECT_GIFT = 7
    LOCK_GIFT = 8
    CHECK_FALSE_GIFT = 9
    FINISH_LOCK_GIFT = 10
    ESC_SETTINGS_GRAPHICS = 11
    START_CHAR_MAIN = 12

    START_CHAR_WINDOW = 13
    ESC_SETTINGS_FINAL = 14

    CUSTOM_WINDOWS = 15
    SCAN_UNNECESSARY_MENU_DOCK = 16
    LOCK_UNNECESSARY_MENU_DOCK = 17
    UNDOCK = 18
    SCAN_UNNECESSARY_MENU_SPACE = 19
    LOCK_UNNECESSARY_MENU_SPACE = 20
    CUSTOM_OVERVIEW = 21
    STEERING_CONTROL = 22
    SPACE_CUSTOM_WINDOWS = 23
    SCAN_MENU_PROBES_CODE = 24
    CUSTOM_MENU_PROBES_CODE = 25
    SCAN_MENU_PROBES_NAME = 26
    CUSTOM_MENU_PROBES_NAME = 27
    EXIT_PROG = 28


class LogicPositioning:
    INITIALIZING_SECONDS = 3

    state = None
    timestamp = None
    window_position = None

    targets = []
    border_pixels = 11
    titlebar_pixels = 45

    def __init__(self):
        self.state = LogicState.SCAN_START_LAUNCHER
        self.timestamp = time()

    def get_screen_position(self, pos):
        x = pos[0] + self.window_position[0] + self.border_pixels
        y = pos[1] + self.window_position[1] + self.titlebar_pixels
        return x, y

    def update_targets(self, targets):
        self.targets = targets
        return None

    def update_win_pos(self, window_position):
        self.window_position = window_position
        return None

    """ Общие функции.=============================================================================================="""

    async def move_to_target(self):
        """
        Перемещает мышь к обнаруженной цели.
        """
        MouseUtils.move_to(self.get_screen_position(self.targets[0]), 3, 3)
        sleep(random.uniform(0.3, 0.6))
        return None

    async def left_click_user(self):
        """
        Левый клик мышью.
        """
        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))
        return None

    async def move_to_left_click_center_large_x(self):
        """
        Перемещает мышь к обнаруженной цели с большим разбросом по оси 'x' и левый клик.
        """
        MouseUtils.move_to(self.get_screen_position(self.targets[0]), 50, 5)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        return None

    async def click_enter(self):
        """
        Нажимает 'enter'
        """
        pag.keyDown('enter')
        sleep(random.uniform(0.15, 0.35))
        pag.keyUp('enter')
        sleep(random.uniform(0.2, 0.4))
        return None

    async def click_esc(self):
        """
        Нажимает 'esc'
        """
        pag.keyDown('esc')
        sleep(random.uniform(0.15, 0.35))
        pag.keyUp('esc')
        sleep(random.uniform(0.2, 0.4))
        return None

    async def click_alt_tab(self):
        """
        Нажимает 'alt + tab'
        """
        pag.keyDown('alt')
        sleep(random.uniform(0.8, 1.2))
        pag.keyDown('tab')
        sleep(random.uniform(0.2, 0.4))
        pag.keyUp('tab')
        sleep(random.uniform(0.3, 0.5))
        pag.keyUp('alt')
        sleep(random.uniform(0.2, 0.4))
        return None

    """ Специальные функции.========================================================================================"""
    async def success_gift(self):
        """
        Наводит мышь на кнопку, что бы забрать подарки
        """
        MouseUtils.move_to(self.get_screen_position((1340, 815)), 5, 2)
        sleep(random.uniform(0.3, 0.6))
        return None

    async def char_select_main(self):
        """
        Выбирает главного персонажа при запуске.
        """
        MouseUtils.move_to(self.get_screen_position((675, 500)), 100, 300)
        sleep(random.uniform(0.3, 0.6))
        return None

    async def removes_banner(self):
        """
        Перемещает мышь в случайную позицию и кликает что бы убрать баннер.
        """
        MouseUtils.move_to(self.get_screen_position((1000, 140)), 600, 50)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        return None

    async def undock(self):
        """
        Корабль покидает станцию.
        """
        pag.keyDown('space')
        sleep(random.uniform(0.15, 0.35))
        pag.keyUp('space')
        sleep(random.uniform(0.2, 0.4))
        return None

    async def on_off_graphics(self):
        pag.keyDown('ctrl')
        sleep(random.uniform(0.3, 0.5))
        pag.keyDown('shift')
        sleep(random.uniform(0.8, 1.2))
        pag.keyDown('f9')
        sleep(random.uniform(0.2, 0.3))
        pag.keyUp('f9')
        sleep(random.uniform(0.3, 0.5))
        pag.keyUp('shift')
        sleep(random.uniform(0.3, 0.5))
        pag.keyUp('ctrl')
        sleep(random.uniform(0.7, 1.1))
        return None

    async def ship_stop(self):
        pag.keyDown('ctrl')
        sleep(random.uniform(0.3, 0.5))
        pag.keyDown('space')
        sleep(random.uniform(0.8, 1.2))
        return None

    async def first_graphics_setup(self):
        """Настройка левой колонны меню Дисплей и графика.__________________________________________________________"""
        MouseUtils.move_to(self.get_screen_position((518, 605)), 3, 3)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((518, 630)), 3, 3)
        sleep(random.uniform(0.2, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((518, 700)), 3, 3)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))

        """Настройка средней колонны меню Дисплей и графика.________________________________________________________"""
        for _ in range(278, 495, 24):
            MouseUtils.move_to(self.get_screen_position((870, _)), 20, 3)
            sleep(random.uniform(0.3, 0.6))

            pag.mouseDown((pag.position()), button='left')
            sleep(random.uniform(0.2, 0.4))
            pag.mouseUp((pag.position()), button='left')
            sleep(random.uniform(0.2, 0.4))

        for _ in range(665, 696, 30):
            MouseUtils.move_to(self.get_screen_position((1025, _)), 15, 3)
            sleep(random.uniform(0.3, 0.6))

            pag.mouseDown((pag.position()), button='left')
            sleep(random.uniform(0.2, 0.4))
            pag.mouseUp((pag.position()), button='left')
            sleep(random.uniform(0.2, 0.4))

        """Настройка правой колонны меню Дисплей и графика._________________________________________________________"""
        MouseUtils.move_to(self.get_screen_position((1340, 320)), 15, 3)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))

        for _ in range(356, 501, 36):
            MouseUtils.move_to(self.get_screen_position((1340, _)), 15, 3)
            sleep(random.uniform(0.3, 0.6))

            pag.mouseDown((pag.position()), button='left')
            sleep(random.uniform(0.2, 0.4))
            pag.mouseUp((pag.position()), button='left')
            sleep(random.uniform(0.2, 0.4))

            pag.mouseDown((pag.position()), button='left')
            sleep(random.uniform(0.2, 0.4))
            pag.mouseUp((pag.position()), button='left')
            sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((1340, 536)), 15, 3)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))

        """Настройка чатов"""
        MouseUtils.move_to(self.get_screen_position((650, 210)), 3, 3)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((518, 302)), 3, 3)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((518, 475)), 3, 3)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((518, 520)), 3, 3)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))

        """Настройка звуков, левая колонная.________________________________________________________________________"""
        MouseUtils.move_to(self.get_screen_position((695, 210)), 3, 3)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((518, 303)), 3, 3)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((518, 365)), 3, 3)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((722, 462)), 2, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((635, 462)), 10, 5)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((750, 548)), 2, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((810, 548)), 10, 5)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        """Настройка звуков, средняя колонная.______________________________________________________________________"""
        MouseUtils.move_to(self.get_screen_position((826, 257)), 3, 3)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((1030, 280)), 2, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((940, 280)), 10, 5)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((1030, 392)), 2, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((940, 392)), 10, 5)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))

        """Настройка звуков, правая колонная._______________________________________________________________________"""
        MouseUtils.move_to(self.get_screen_position((1134, 258)), 3, 3)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))

        for _ in range(320, 345, 24):
            MouseUtils.move_to(self.get_screen_position((1143, _)), 3, 3)
            sleep(random.uniform(0.3, 0.6))

            pag.mouseDown((pag.position()), button='left')
            sleep(random.uniform(0.2, 0.4))
            pag.mouseUp((pag.position()), button='left')
            sleep(random.uniform(0.2, 0.4))

        for _ in range(453, 502, 48):
            MouseUtils.move_to(self.get_screen_position((1143, _)), 3, 3)
            sleep(random.uniform(0.3, 0.6))

            pag.mouseDown((pag.position()), button='left')
            sleep(random.uniform(0.2, 0.4))
            pag.mouseUp((pag.position()), button='left')
            sleep(random.uniform(0.2, 0.4))

        for _ in range(597, 814, 24):
            MouseUtils.move_to(self.get_screen_position((1143, _)), 3, 3)
            sleep(random.uniform(0.3, 0.6))

            pag.mouseDown((pag.position()), button='left')
            sleep(random.uniform(0.2, 0.4))
            pag.mouseUp((pag.position()), button='left')
            sleep(random.uniform(0.2, 0.4))

        """Первичная настройка общих параметров.____________________________________________________________________"""
        MouseUtils.move_to(self.get_screen_position((780, 210)), 10, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((663, 384)), 2, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((708, 384)), 5, 5)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))

        """Редактирование горячих клавиш, Управление окнами.________________________________________________________"""
        MouseUtils.move_to(self.get_screen_position((905, 210)), 10, 3)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))

        """Список наблюдения ALT+V._________________________________________________________________________________"""
        MouseUtils.move_to(self.get_screen_position((700, 310)), 50, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='right')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='right')
        sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to((pag.position()[0] + 70, pag.position()[1] + 20), 10, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))

        pag.keyDown('alt')
        sleep(random.uniform(0.8, 1.2))
        pag.keyDown('v')
        sleep(random.uniform(0.4, 0.6))
        pag.keyUp('v')
        sleep(random.uniform(0.3, 0.5))
        pag.keyUp('alt')
        sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((860, 635)), 20, 5)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))

        """прокрутка________________________________________________________________________________________________"""
        for _ in range(2):
            sleep(random.uniform(0.8, 1.3))
            for _ in range(7):
                pag.scroll(-100)
                sleep(random.uniform(0.035, 0.039))

        """Места ALT+L._____________________________________________________________________________________________"""
        MouseUtils.move_to(self.get_screen_position((700, 470)), 50, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='right')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='right')
        sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to((pag.position()[0] + 70, pag.position()[1] + 20), 10, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))

        pag.keyDown('alt')
        sleep(random.uniform(0.8, 1.2))
        pag.keyDown('l')
        sleep(random.uniform(0.4, 0.6))
        pag.keyUp('l')
        sleep(random.uniform(0.3, 0.5))
        pag.keyUp('alt')
        sleep(random.uniform(0.2, 0.4))

        """Местные координаты L.____________________________________________________________________________________"""
        pag.mouseDown((pag.position()), button='right')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='right')
        sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to((pag.position()[0] + 70, pag.position()[1] + 20), 10, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))

        pag.keyDown('l')
        sleep(random.uniform(0.3, 0.5))
        pag.keyUp('l')
        sleep(random.uniform(0.3, 0.5))

        """прокрутка________________________________________________________________________________________________"""
        for _ in range(3):
            sleep(random.uniform(0.8, 1.3))
            for _ in range(8):
                pag.scroll(-100)
                sleep(random.uniform(0.035, 0.039))

        """Схема кораблей ALT+S.____________________________________________________________________________________"""
        MouseUtils.move_to(self.get_screen_position((700, 575)), 50, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='right')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='right')
        sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to((pag.position()[0] + 70, pag.position()[1] + 20), 10, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))

        pag.keyDown('alt')
        sleep(random.uniform(0.8, 1.2))
        pag.keyDown('s')
        sleep(random.uniform(0.4, 0.6))
        pag.keyUp('s')
        sleep(random.uniform(0.3, 0.5))
        pag.keyUp('alt')
        sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((860, 635)), 20, 5)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))

        """Штаб флотаALT+Q._________________________________________________________________________________________"""
        MouseUtils.move_to(self.get_screen_position((700, 761)), 50, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='right')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='right')
        sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to((pag.position()[0] + 70, pag.position()[1] + 20), 10, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))

        pag.keyDown('alt')
        sleep(random.uniform(0.8, 1.2))
        pag.keyDown('q')
        sleep(random.uniform(0.4, 0.6))
        pag.keyUp('q')
        sleep(random.uniform(0.3, 0.5))
        pag.keyUp('alt')
        sleep(random.uniform(0.2, 0.4))

        """Общие.___________________________________________________________________________________________________"""
        MouseUtils.move_to(self.get_screen_position((745, 250)), 5, 5)

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))

        """Покинуть станцию SPACE.__________________________________________________________________________________"""
        MouseUtils.move_to(self.get_screen_position((700, 511)), 50, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='right')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='right')
        sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to((pag.position()[0] + 70, pag.position()[1] + 20), 10, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))

        pag.keyDown('space')
        sleep(random.uniform(0.3, 0.5))
        pag.keyUp('space')
        sleep(random.uniform(0.3, 0.5))

        MouseUtils.move_to(self.get_screen_position((860, 635)), 20, 5)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))

        """Управление дронами.______________________________________________________________________________________"""
        MouseUtils.move_to(self.get_screen_position((1140, 252)), 10, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))

        """Возврат дронов в отсек R.________________________________________________________________________________"""
        MouseUtils.move_to(self.get_screen_position((700, 352)), 50, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='right')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='right')
        sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to((pag.position()[0] + 70, pag.position()[1] + 20), 10, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))

        pag.keyDown('r')
        sleep(random.uniform(0.3, 0.5))
        pag.keyUp('r')
        sleep(random.uniform(0.3, 0.5))

        """Запуск дронов G._________________________________________________________________________________________"""
        MouseUtils.move_to(self.get_screen_position((700, 393)), 50, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='right')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='right')
        sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to((pag.position()[0] + 70, pag.position()[1] + 20), 10, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))

        pag.keyDown('g')
        sleep(random.uniform(0.3, 0.5))
        pag.keyUp('g')
        sleep(random.uniform(0.3, 0.5))
        sleep(5)
        return None

    async def final_graphics_setup(self):
        """Настройка меню Общие параметры, правая колонна.__________________________________________________________"""
        MouseUtils.move_to(self.get_screen_position((780, 210)), 10, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((1408, 303)), 2, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((1245, 303)), 10, 5)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((1408, 348)), 2, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((1245, 348)), 10, 5)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((1275, 417)), 30, 3)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to((pag.position()[0], pag.position()[1] + 95), 30, 3)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((1134, 453)), 3, 3)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))
        return None

    async def custom_windows(self):
        """Фиксируем окно станции.__________________________________________________________________________________"""
        MouseUtils.move_to(self.get_screen_position((1863, 33)), 2, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((1750, 63)), 10, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        """Фиксируем панель неоком._________________________________________________________________________________"""
        MouseUtils.move_to(self.get_screen_position((25, 760)), 3, 3)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='right')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='right')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((150, 780)), 20, 3)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        """Настройка окна чатов с помощью размера окна журнала._____________________________________________________"""
        pag.keyDown('alt')
        sleep(random.uniform(0.8, 1.2))
        pag.keyDown('j')
        sleep(random.uniform(0.4, 0.6))
        pag.keyUp('j')
        sleep(random.uniform(0.3, 0.5))
        pag.keyUp('alt')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((1110, 415)), 5, 5)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((926, 789)), 3, 3)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((250, 715)), 100, 3)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((250, 765)), 50, 3)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((473, 782)), 2, 3)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((530, 775)), 5, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((110, 780)), 10, 3)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        """Настройка окна склада.___________________________________________________________________________________"""
        pag.keyDown('alt')
        sleep(random.uniform(0.8, 1.2))
        pag.keyDown('c')
        sleep(random.uniform(0.4, 0.6))
        pag.keyUp('c')
        sleep(random.uniform(0.3, 0.5))
        pag.keyUp('alt')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((200, 330)), 10, 3)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to((pag.position()[0] - 15, pag.position()[1]), 2, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((599, 333)), 2, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((750, 402)), 50, 3)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        """Настройка окна журнала.__________________________________________________________________________________"""
        MouseUtils.move_to(self.get_screen_position((925, 790)), 5, 5)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((1075, 340)), 5, 5)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((1187, 612)), 1, 1)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((1625, 762)), 3, 3)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((687, 742)), 3, 3)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((1559, 340)), 2, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((1700, 370)), 50, 3)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        pag.keyDown('alt')
        sleep(random.uniform(0.8, 1.2))
        pag.keyDown('j')
        sleep(random.uniform(0.4, 0.6))
        pag.keyUp('j')
        sleep(random.uniform(0.3, 0.5))
        pag.keyUp('alt')
        sleep(random.uniform(0.7, 1.2))

        """Фиксируем окно Личное дело пилота._______________________________________________________________________"""
        pag.keyDown('alt')
        sleep(random.uniform(0.8, 1.2))
        pag.keyDown('a')
        sleep(random.uniform(0.4, 0.6))
        pag.keyUp('a')
        sleep(random.uniform(0.3, 0.5))
        pag.keyUp('alt')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((1512, 183)), 2, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((1650, 210)), 30, 3)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        pag.keyDown('alt')
        sleep(random.uniform(0.8, 1.2))
        pag.keyDown('a')
        sleep(random.uniform(0.4, 0.6))
        pag.keyUp('a')
        sleep(random.uniform(0.3, 0.5))
        pag.keyUp('alt')
        sleep(random.uniform(0.7, 1.2))

        """Фиксируем окно Кошелёк.__________________________________________________________________________________"""
        pag.keyDown('alt')
        sleep(random.uniform(0.8, 1.2))
        pag.keyDown('w')
        sleep(random.uniform(0.4, 0.6))
        pag.keyUp('w')
        sleep(random.uniform(0.3, 0.5))
        pag.keyUp('alt')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((1270, 267)), 2, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((1430, 297)), 30, 3)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        pag.keyDown('alt')
        sleep(random.uniform(0.8, 1.2))
        pag.keyDown('w')
        sleep(random.uniform(0.4, 0.6))
        pag.keyUp('w')
        sleep(random.uniform(0.3, 0.5))
        pag.keyUp('alt')
        sleep(random.uniform(0.7, 1.2))

        """Фиксируем окно Контакты._________________________________________________________________________________"""
        pag.keyDown('alt')
        sleep(random.uniform(0.8, 1.2))
        pag.keyDown('e')
        sleep(random.uniform(0.4, 0.6))
        pag.keyUp('e')
        sleep(random.uniform(0.3, 0.5))
        pag.keyUp('alt')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((1195, 317)), 2, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((1330, 347)), 30, 3)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        pag.keyDown('alt')
        sleep(random.uniform(0.8, 1.2))
        pag.keyDown('e')
        sleep(random.uniform(0.4, 0.6))
        pag.keyUp('e')
        sleep(random.uniform(0.3, 0.5))
        pag.keyUp('alt')
        sleep(random.uniform(0.7, 1.2))

        """Настраиваем окно Торговая система._______________________________________________________________________"""
        pag.keyDown('alt')
        sleep(random.uniform(0.8, 1.2))
        pag.keyDown('r')
        sleep(random.uniform(0.4, 0.6))
        pag.keyUp('r')
        sleep(random.uniform(0.3, 0.5))
        pag.keyUp('alt')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((900, 158)), 100, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((1000, 13)), 100, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((900, 920)), 100, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((1000, 1067)), 100, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((1407, 500)), 2, 300)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((1905, 500)), 2, 300)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((702, 800)), 1, 100)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((850, 700)), 2, 300)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((830, 102)), 3, 3)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((840, 132)), 2, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((1839, 35)), 2, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((1750, 63)), 50, 3)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((650, 495)), 50, 3)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((650, 540)), 50, 3)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((650, 565)), 50, 3)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((1070, 237)), 10, 3)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((1070, 672)), 10, 3)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((1630, 68)), 30, 3)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        """Настройка окна Заказы в торговой системе.________________________________________________________________"""
        MouseUtils.move_to(self.get_screen_position((662, 550)), 2, 100)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((65, 550)), 2, 100)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((650, 787)), 100, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        #
        MouseUtils.move_to(self.get_screen_position((680, 1063)), 100, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((600, 294)), 100, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((700, 16)), 100, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((1255, 550)), 2, 300)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        #
        MouseUtils.move_to(self.get_screen_position((1825, 550)), 2, 300)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((1763, 43)), 2, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((1750, 70)), 30, 3)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((1811, 43)), 3, 3)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        """Настройка окна Оптовая покупка.__________________________________________________________________________"""
        MouseUtils.move_to(self.get_screen_position((1810, 70)), 30, 3)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((950, 350)), 100, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((950, 15)), 100, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((950, 730)), 100, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        #
        MouseUtils.move_to(self.get_screen_position((950, 1065)), 100, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((704, 600)), 2, 300)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((510, 650)), 2, 300)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((1155, 35)), 2, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((1300, 65)), 50, 3)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((1203, 35)), 3, 3)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        """Настройка окна Покупка товаров.__________________________________________________________________________"""
        MouseUtils.move_to(self.get_screen_position((1080, 258)), 20, 3)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='right')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='right')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((1180, 277)), 5, 3)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((1140, 745)), 10, 5)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((1130, 493)), 2, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((1250, 525)), 20, 3)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((745, 960)), 3, 3)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((1177, 493)), 3, 3)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        pag.keyDown('alt')
        sleep(random.uniform(0.8, 1.2))
        pag.keyDown('r')
        sleep(random.uniform(0.4, 0.6))
        pag.keyUp('r')
        sleep(random.uniform(0.3, 0.5))
        pag.keyUp('alt')
        sleep(random.uniform(0.7, 1.2))

        """Настройка окна Оснащение кораблей._______________________________________________________________________"""
        pag.keyDown('alt')
        sleep(random.uniform(0.8, 1.2))
        pag.keyDown('f')
        sleep(random.uniform(0.4, 0.6))
        pag.keyUp('f')
        sleep(random.uniform(0.3, 0.5))
        pag.keyUp('alt')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((1855, 228)), 2, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((1750, 257)), 30, 3)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        for _ in range(435, 338, -24):
            MouseUtils.move_to(self.get_screen_position((1750, _)), 20, 3)
            sleep(random.uniform(0.3, 0.6))

            pag.mouseDown((pag.position()), button='left')
            sleep(random.uniform(0.2, 0.4))
            pag.mouseUp((pag.position()), button='left')
            sleep(random.uniform(0.7, 1.2))

        pag.keyDown('alt')
        sleep(random.uniform(0.8, 1.2))
        pag.keyDown('f')
        sleep(random.uniform(0.4, 0.6))
        pag.keyUp('f')
        sleep(random.uniform(0.3, 0.5))
        pag.keyUp('alt')
        sleep(random.uniform(0.7, 1.2))

        """Фиксируем окно База личного имущества.___________________________________________________________________"""
        pag.keyDown('alt')
        sleep(random.uniform(0.8, 1.2))
        pag.keyDown('t')
        sleep(random.uniform(0.4, 0.6))
        pag.keyUp('t')
        sleep(random.uniform(0.3, 0.5))
        pag.keyUp('alt')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((1170, 342)), 2, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((1300, 372)), 30, 3)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        pag.keyDown('alt')
        sleep(random.uniform(0.8, 1.2))
        pag.keyDown('t')
        sleep(random.uniform(0.4, 0.6))
        pag.keyUp('t')
        sleep(random.uniform(0.3, 0.5))
        pag.keyUp('alt')
        sleep(random.uniform(0.7, 1.2))

        """Фиксируем окно Выдача предметов._________________________________________________________________________"""
        pag.keyDown('alt')
        sleep(random.uniform(0.8, 1.2))
        pag.keyDown('y')
        sleep(random.uniform(0.4, 0.6))
        pag.keyUp('y')
        sleep(random.uniform(0.3, 0.5))
        pag.keyUp('alt')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((1275, 238)), 2, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((1400, 270)), 30, 3)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        pag.keyDown('alt')
        sleep(random.uniform(0.8, 1.2))
        pag.keyDown('y')
        sleep(random.uniform(0.4, 0.6))
        pag.keyUp('y')
        sleep(random.uniform(0.3, 0.5))
        pag.keyUp('alt')
        sleep(random.uniform(0.7, 1.2))

        """Фиксируем окно Почта.____________________________________________________________________________________"""
        pag.keyDown('alt')
        sleep(random.uniform(0.8, 1.2))
        pag.keyDown('i')
        sleep(random.uniform(0.4, 0.6))
        pag.keyUp('i')
        sleep(random.uniform(0.3, 0.5))
        pag.keyUp('alt')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((1295, 267)), 2, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((1400, 295)), 0, 0)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        pag.keyDown('alt')
        sleep(random.uniform(0.8, 1.2))
        pag.keyDown('i')
        sleep(random.uniform(0.4, 0.6))
        pag.keyUp('i')
        sleep(random.uniform(0.3, 0.5))
        pag.keyUp('alt')
        sleep(random.uniform(0.7, 1.2))

        """Фиксируем окно Места.____________________________________________________________________________________"""
        pag.keyDown('alt')
        sleep(random.uniform(0.8, 1.2))
        pag.keyDown('l')
        sleep(random.uniform(0.4, 0.6))
        pag.keyUp('l')
        sleep(random.uniform(0.3, 0.5))
        pag.keyUp('alt')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((1120, 340)), 2, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((1280, 413)), 30, 3)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        pag.keyDown('alt')
        sleep(random.uniform(0.8, 1.2))
        pag.keyDown('l')
        sleep(random.uniform(0.4, 0.6))
        pag.keyUp('l')
        sleep(random.uniform(0.3, 0.5))
        pag.keyUp('alt')
        sleep(random.uniform(0.7, 1.2))
        return None

    async def customization_overview(self):
        """Настройки Овервью._______________________________________________________________________________________"""
        MouseUtils.move_to(self.get_screen_position((1863, 208)), 2, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((1700, 418)), 20, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((1155, 258)), 2, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((1300, 288)), 30, 3)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((1040, 333)), 7, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((840, 815)), 30, 5)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((900, 542)), 10, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((1111, 538)), 3, 3)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((1185, 700)), 10, 5)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((970, 333)), 7, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((1017, 479)), 3, 3)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((890, 333)), 10, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        for _ in range(559, 604, 22):
            MouseUtils.move_to(self.get_screen_position((950, _)), 100, 3)
            sleep(random.uniform(0.3, 0.6))

            pag.mouseDown((pag.position()), button='right')
            sleep(random.uniform(0.2, 0.4))
            pag.mouseUp((pag.position()), button='right')
            sleep(random.uniform(0.7, 1.2))

            MouseUtils.move_to((pag.position()[0] + 100, pag.position()[1] + 17), 30, 3)
            sleep(random.uniform(0.3, 0.6))

            pag.mouseDown((pag.position()), button='left')
            sleep(random.uniform(0.2, 0.4))
            pag.mouseUp((pag.position()), button='left')
            sleep(random.uniform(0.7, 1.2))

        """прокрутка"""
        for _ in range(2):
            sleep(random.uniform(0.8, 1.3))
            for _ in range(7):
                pag.scroll(-100)
                sleep(random.uniform(0.035, 0.039))

        for _ in range(650, 695, 22):
            MouseUtils.move_to(self.get_screen_position((950, _)), 100, 3)
            sleep(random.uniform(0.3, 0.6))

            pag.mouseDown((pag.position()), button='right')
            sleep(random.uniform(0.2, 0.4))
            pag.mouseUp((pag.position()), button='right')
            sleep(random.uniform(0.7, 1.2))

            MouseUtils.move_to((pag.position()[0] + 100, pag.position()[1] + 17), 30, 3)
            sleep(random.uniform(0.3, 0.6))

            pag.mouseDown((pag.position()), button='left')
            sleep(random.uniform(0.2, 0.4))
            pag.mouseUp((pag.position()), button='left')
            sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((775, 528)), 5, 5)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((950, 622)), 100, 3)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='right')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='right')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to((pag.position()[0] + 100, pag.position()[1] + 17), 30, 3)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((950, 750)), 100, 3)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='right')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='right')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to((pag.position()[0] + 100, pag.position()[1] + 17), 30, 3)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((1203, 258)), 3, 3)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        """Настройка позиции Овервью._______________________________________________________________________________"""
        MouseUtils.move_to(self.get_screen_position((1341, 550)), 2, 150)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((1560, 550)), 2, 150)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((1740, 878)), 20, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((1740, 865)), 20, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((1863, 208)), 2, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((1725, 280)), 50, 3)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        """Настройка позиции окна дронов.___________________________________________________________________________"""
        MouseUtils.move_to(self.get_screen_position((1341, 970)), 2, 20)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((1560, 970)), 20, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((1863, 887)), 2, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((1650, 837)), 50, 3)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        """Настройка позиции окна выбора и взаимодействия с целью.__________________________________________________"""
        MouseUtils.move_to(self.get_screen_position((1341, 100)), 2, 10)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((1560, 100)), 2, 10)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((1863, 35)), 2, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((1725, 105)), 20, 3)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))
        return None

    async def steering_control(self):
        """Настройка меню рулевого управления.______________________________________________________________________"""
        MouseUtils.move_to(self.get_screen_position((1030, 1054)), 2, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((1150, 707)), 30, 3)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((1150, 750)), 30, 3)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((1150, 833)), 30, 3)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((1150, 933)), 30, 3)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((1150, 1028)), 30, 3)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        """Режим перемещения сообщений._____________________________________________________________________________"""
        MouseUtils.move_to(self.get_screen_position((820, 10)), 3, 3)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((380, 10)), 3, 3)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((770, 340)), 2, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((380, 120)), 3, 3)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((1030, 1054)), 2, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((1150, 1028)), 30, 3)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        """Фиксируем список кораблей на прицеле.____________________________________________________________________"""
        MouseUtils.move_to(self.get_screen_position((1725, 260)), 25, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.keyDown('ctrl')
        sleep(random.uniform(0.4, 0.8))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.3, 0.5))

        pag.keyUp('ctrl')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((1541, 15)), 0, 0)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='right')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='right')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((1725, 33)), 30, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))
        return None

    async def space_custom_windows(self):
        """Настройка позиции окна склада.___________________________________________________________________________"""
        pag.keyDown('alt')
        sleep(random.uniform(0.8, 1.2))
        pag.keyDown('c')
        sleep(random.uniform(0.4, 0.6))
        pag.keyUp('c')
        sleep(random.uniform(0.3, 0.5))
        pag.keyUp('alt')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((200, 330)), 10, 3)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to((pag.position()[0] - 15, pag.position()[1]), 2, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((599, 333)), 2, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((750, 402)), 50, 3)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        pag.keyDown('alt')
        sleep(random.uniform(0.8, 1.2))
        pag.keyDown('c')
        sleep(random.uniform(0.4, 0.6))
        pag.keyUp('c')
        sleep(random.uniform(0.3, 0.5))
        pag.keyUp('alt')
        sleep(random.uniform(0.7, 1.2))

        """Настройка позиции окна местных координат.________________________________________________________________"""
        pag.keyDown('l')
        sleep(random.uniform(0.3, 0.5))
        pag.keyUp('l')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((965, 601)), 15, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((965, 762)), 15, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((850, 490)), 3, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((80, 490)), 2, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((190, 479)), 20, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((190, 360)), 20, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((317, 560)), 2, 40)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((400, 560)), 2, 40)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((340, 375)), 2, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((500, 443)), 100, 3)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        """Настройка окна пеленгатора.______________________________________________________________________________"""
        pag.keyDown('alt')
        sleep(random.uniform(0.8, 1.2))
        pag.keyDown('d')
        sleep(random.uniform(0.4, 0.6))
        pag.keyUp('d')
        sleep(random.uniform(0.3, 0.5))
        pag.keyUp('alt')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((1858, 50)), 2, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        pag.keyDown('f9')
        sleep(random.uniform(0.4, 0.6))
        pag.keyUp('f9')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((950, 368)), 50, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((950, 192)), 50, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((1157, 450)), 2, 50)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((1557, 450)), 2, 50)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((763, 450)), 2, 50)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((1417, 450)), 2, 50)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((1400, 712)), 20, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((1400, 767)), 20, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((1440, 751)), 2, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((1500, 750)), 15, 10)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((1491, 209)), 2, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((1650, 278)), 50, 3)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        """Настройка окна разведзондов._____________________________________________________________________________"""
        pag.keyDown('alt')
        sleep(random.uniform(0.8, 1.2))
        pag.keyDown('p')
        sleep(random.uniform(0.4, 0.6))
        pag.keyUp('p')
        sleep(random.uniform(0.3, 0.5))
        pag.keyUp('alt')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((1858, 50)), 2, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        pag.keyDown('f9')
        sleep(random.uniform(0.4, 0.6))
        pag.keyUp('f9')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((960, 343)), 50, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((960, 358)), 50, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((1157, 550)), 2, 30)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((1257, 550)), 0, 30)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((1050, 737)), 50, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((1050, 765)), 50, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((763, 550)), 2, 50)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((850, 550)), 2, 50)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((1192, 376)), 2, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((1350, 445)), 50, 3)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        """Настройка окна флота.____________________________________________________________________________________"""
        pag.keyDown('alt')
        sleep(random.uniform(0.8, 1.2))
        pag.keyDown('q')
        sleep(random.uniform(0.4, 0.6))
        pag.keyUp('q')
        sleep(random.uniform(0.3, 0.5))
        pag.keyUp('alt')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((950, 345)), 100, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((950, 192)), 100, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((713, 450)), 2, 50)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((402, 450)), 2, 50)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((800, 736)), 100, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((800, 765)), 100, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((1208, 450)), 2, 50)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((845, 450)), 2, 50)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((779, 217)), 2, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((950, 287)), 100, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        """Настройка созданного флота.______________________________________________________________________________"""
        MouseUtils.move_to(self.get_screen_position((470, 735)), 10, 5)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        for _ in range(4):
            MouseUtils.move_to(self.get_screen_position((580, 285)), 10, 5)
            sleep(random.uniform(0.3, 0.6))

            pag.mouseDown((pag.position()), button='right')
            sleep(random.uniform(0.2, 0.4))
            pag.mouseUp((pag.position()), button='right')
            sleep(random.uniform(0.7, 1.2))

            MouseUtils.move_to(self.get_screen_position((680, 428)), 10, 3)
            sleep(random.uniform(0.3, 0.6))

            pag.mouseDown((pag.position()), button='left')
            sleep(random.uniform(0.2, 0.4))
            pag.mouseUp((pag.position()), button='left')
            sleep(random.uniform(0.7, 1.2))

        counter_wings = 1
        for _ in range(325, 554, 57):
            MouseUtils.move_to(self.get_screen_position((630, _)), 10, 3)
            sleep(random.uniform(0.3, 0.6))

            pag.mouseDown((pag.position()), button='right')
            sleep(random.uniform(0.2, 0.4))
            pag.mouseUp((pag.position()), button='right')
            sleep(random.uniform(0.7, 1.2))

            MouseUtils.move_to((pag.position()[0] + 70, pag.position()[1] + 40), 7, 2)
            sleep(random.uniform(0.3, 0.6))

            pag.mouseDown((pag.position()), button='left')
            sleep(random.uniform(0.2, 0.4))
            pag.mouseUp((pag.position()), button='left')
            sleep(random.uniform(0.7, 1.2))

            pag.keyDown('W')
            sleep(random.uniform(0.4, 0.6))
            pag.keyUp('W')
            sleep(random.uniform(0.9, 1.4))
            pag.keyDown('i')
            sleep(random.uniform(0.4, 0.6))
            pag.keyUp('i')
            sleep(random.uniform(0.9, 1.4))
            pag.keyDown('n')
            sleep(random.uniform(0.4, 0.6))
            pag.keyUp('n')
            sleep(random.uniform(0.9, 1.4))
            pag.keyDown('g')
            sleep(random.uniform(0.4, 0.6))
            pag.keyUp('g')
            sleep(random.uniform(0.9, 1.4))
            pag.keyDown('_')
            sleep(random.uniform(0.4, 0.6))
            pag.keyUp('_')
            sleep(random.uniform(0.9, 1.4))
            pag.keyDown(f'{counter_wings}')
            sleep(random.uniform(0.4, 0.6))
            pag.keyUp(f'{counter_wings}')
            sleep(random.uniform(0.9, 1.4))
            pag.keyDown('enter')
            sleep(random.uniform(0.4, 0.6))
            pag.keyUp('enter')
            sleep(random.uniform(0.9, 1.4))

            counter_wings += 1

        for _ in range(553, 324, -57):
            for __ in range(4):
                MouseUtils.move_to(self.get_screen_position((630, _)), 10, 3)
                sleep(random.uniform(0.3, 0.6))

                pag.mouseDown((pag.position()), button='right')
                sleep(random.uniform(0.2, 0.4))
                pag.mouseUp((pag.position()), button='right')
                sleep(random.uniform(0.7, 1.2))

                MouseUtils.move_to((pag.position()[0] + 80, pag.position()[1] + 60), 7, 2)
                sleep(random.uniform(0.3, 0.6))

                pag.mouseDown((pag.position()), button='left')
                sleep(random.uniform(0.2, 0.4))
                pag.mouseUp((pag.position()), button='left')
                sleep(random.uniform(0.7, 1.2))

        counter_squad = 1
        for _ in range(355, 498, 142):
            for __ in range(_, _ + 81, 20):
                MouseUtils.move_to(self.get_screen_position((630, __)), 10, 2)
                sleep(random.uniform(0.3, 0.6))

                pag.mouseDown((pag.position()), button='right')
                sleep(random.uniform(0.2, 0.4))
                pag.mouseUp((pag.position()), button='right')
                sleep(random.uniform(0.7, 1.2))

                MouseUtils.move_to((pag.position()[0] + 80, pag.position()[1] + 20), 7, 2)
                sleep(random.uniform(0.3, 0.6))

                pag.mouseDown((pag.position()), button='left')
                sleep(random.uniform(0.2, 0.4))
                pag.mouseUp((pag.position()), button='left')
                sleep(random.uniform(0.7, 1.2))

                pag.keyDown('s')
                sleep(random.uniform(0.4, 0.6))
                pag.keyUp('s')
                sleep(random.uniform(0.9, 1.4))
                pag.keyDown('q')
                sleep(random.uniform(0.4, 0.6))
                pag.keyUp('q')
                sleep(random.uniform(0.9, 1.4))
                pag.keyDown('u')
                sleep(random.uniform(0.4, 0.6))
                pag.keyUp('u')
                sleep(random.uniform(0.9, 1.4))
                pag.keyDown('a')
                sleep(random.uniform(0.4, 0.6))
                pag.keyUp('a')
                sleep(random.uniform(0.9, 1.4))
                pag.keyDown('d')
                sleep(random.uniform(0.4, 0.6))
                pag.keyUp('d')
                sleep(random.uniform(0.9, 1.4))
                pag.keyDown('_')
                sleep(random.uniform(0.4, 0.6))
                pag.keyUp('_')
                sleep(random.uniform(0.9, 1.4))
                if counter_squad < 10:
                    pag.keyDown(f'{counter_squad}')
                    sleep(random.uniform(0.4, 0.6))
                    pag.keyUp(f'{counter_squad}')
                    sleep(random.uniform(0.9, 1.4))
                    pag.keyDown('enter')
                    sleep(random.uniform(0.4, 0.6))
                    pag.keyUp('enter')
                    sleep(random.uniform(0.9, 1.4))
                else:
                    pag.keyDown(f'{counter_squad // 10}')
                    sleep(random.uniform(0.4, 0.6))
                    pag.keyUp(f'{counter_squad // 10}')
                    sleep(random.uniform(0.9, 1.4))
                    pag.keyDown(f'{counter_squad % 10}')
                    sleep(random.uniform(0.4, 0.6))
                    pag.keyUp(f'{counter_squad % 10}')
                    sleep(random.uniform(0.9, 1.4))
                    pag.keyDown('enter')
                    sleep(random.uniform(0.4, 0.6))
                    pag.keyUp('enter')
                    sleep(random.uniform(0.9, 1.4))

                counter_squad += 1

        """прокрутка"""
        for _ in range(2):
            sleep(random.uniform(0.8, 1.3))
            for _ in range(5):
                pag.scroll(-100)
                sleep(random.uniform(0.035, 0.039))

        counter_squad = 11
        for _ in range(315, 600, 142):
            for __ in range(_, _ + 81, 20):
                MouseUtils.move_to(self.get_screen_position((630, __)), 10, 2)
                sleep(random.uniform(0.3, 0.6))

                pag.mouseDown((pag.position()), button='right')
                sleep(random.uniform(0.2, 0.4))
                pag.mouseUp((pag.position()), button='right')
                sleep(random.uniform(0.7, 1.2))

                MouseUtils.move_to((pag.position()[0] + 80, pag.position()[1] + 20), 7, 2)
                sleep(random.uniform(0.3, 0.6))

                pag.mouseDown((pag.position()), button='left')
                sleep(random.uniform(0.2, 0.4))
                pag.mouseUp((pag.position()), button='left')
                sleep(random.uniform(0.7, 1.2))

                pag.keyDown('s')
                sleep(random.uniform(0.4, 0.6))
                pag.keyUp('s')
                sleep(random.uniform(0.9, 1.4))
                pag.keyDown('q')
                sleep(random.uniform(0.4, 0.6))
                pag.keyUp('q')
                sleep(random.uniform(0.9, 1.4))
                pag.keyDown('u')
                sleep(random.uniform(0.4, 0.6))
                pag.keyUp('u')
                sleep(random.uniform(0.9, 1.4))
                pag.keyDown('a')
                sleep(random.uniform(0.4, 0.6))
                pag.keyUp('a')
                sleep(random.uniform(0.9, 1.4))
                pag.keyDown('d')
                sleep(random.uniform(0.4, 0.6))
                pag.keyUp('d')
                sleep(random.uniform(0.9, 1.4))
                pag.keyDown('_')
                sleep(random.uniform(0.4, 0.6))
                pag.keyUp('_')
                sleep(random.uniform(0.9, 1.4))
                if counter_squad < 10:
                    pag.keyDown(f'{counter_squad}')
                    sleep(random.uniform(0.4, 0.6))
                    pag.keyUp(f'{counter_squad}')
                    sleep(random.uniform(0.9, 1.4))
                    pag.keyDown('enter')
                    sleep(random.uniform(0.4, 0.6))
                    pag.keyUp('enter')
                    sleep(random.uniform(0.9, 1.4))
                else:
                    pag.keyDown(f'{counter_squad // 10}')
                    sleep(random.uniform(0.4, 0.6))
                    pag.keyUp(f'{counter_squad // 10}')
                    sleep(random.uniform(0.9, 1.4))
                    pag.keyDown(f'{counter_squad % 10}')
                    sleep(random.uniform(0.4, 0.6))
                    pag.keyUp(f'{counter_squad % 10}')
                    sleep(random.uniform(0.9, 1.4))
                    pag.keyDown('enter')
                    sleep(random.uniform(0.4, 0.6))
                    pag.keyUp('enter')
                    sleep(random.uniform(0.9, 1.4))

                counter_squad += 1

        MouseUtils.move_to(self.get_screen_position((755, 217)), 2, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((930, 592)), 30, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((755, 217)), 2, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((930, 495)), 30, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        pag.keyDown('m')
        sleep(random.uniform(0.4, 0.6))
        pag.keyUp('m')
        sleep(random.uniform(0.9, 1.4))
        pag.keyDown('e')
        sleep(random.uniform(0.4, 0.6))
        pag.keyUp('e')
        sleep(random.uniform(0.9, 1.4))
        pag.keyDown('_')
        sleep(random.uniform(0.4, 0.6))
        pag.keyUp('_')
        sleep(random.uniform(0.9, 1.4))
        pag.keyDown('f')
        sleep(random.uniform(0.4, 0.6))
        pag.keyUp('f')
        sleep(random.uniform(0.9, 1.4))
        pag.keyDown('l')
        sleep(random.uniform(0.4, 0.6))
        pag.keyUp('l')
        sleep(random.uniform(0.9, 1.4))
        pag.keyDown('e')
        sleep(random.uniform(0.4, 0.6))
        pag.keyUp('e')
        sleep(random.uniform(0.9, 1.4))
        pag.keyDown('e')
        sleep(random.uniform(0.4, 0.6))
        pag.keyUp('e')
        sleep(random.uniform(0.9, 1.4))
        pag.keyDown('t')
        sleep(random.uniform(0.4, 0.6))
        pag.keyUp('t')
        sleep(random.uniform(0.9, 1.4))

        MouseUtils.move_to(self.get_screen_position((850, 585)), 10, 3)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((915, 640)), 10, 3)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((755, 217)), 2, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((930, 647)), 10, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((1195, 495)), 2, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((1335, 525)), 30, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((750, 750)), 10, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((730, 780)), 10, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((1030, 537)), 10, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((1030, 668)), 10, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((1030, 730)), 10, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((910, 940)), 10, 5)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        pag.keyDown('alt')
        sleep(random.uniform(0.8, 1.2))
        pag.keyDown('q')
        sleep(random.uniform(0.4, 0.6))
        pag.keyUp('q')
        sleep(random.uniform(0.3, 0.5))
        pag.keyUp('alt')
        sleep(random.uniform(0.7, 1.2))

        """Настройка окна карты системы.____________________________________________________________________________"""
        pag.keyDown('f9')
        sleep(random.uniform(0.4, 0.6))
        pag.keyUp('f9')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((1128, 17)), 3, 3)
        sleep(random.uniform(0.3, 0.6))

        MouseUtils.move_to(self.get_screen_position((1150, 50)), 3, 3)
        sleep(random.uniform(0.3, 0.6))

        MouseUtils.move_to(self.get_screen_position((1150, 80)), 3, 3)
        sleep(random.uniform(0.3, 0.6))

        MouseUtils.move_to(self.get_screen_position((1150, 110)), 3, 3)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((1725, 600)), 2, 100)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((843, 600)), 2, 100)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((520, 112)), 100, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((520, 358)), 100, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((196, 650)), 2, 50)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((67, 650)), 2, 50)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        pag.keyDown('f9')
        sleep(random.uniform(0.4, 0.6))
        pag.keyUp('f9')
        sleep(random.uniform(0.7, 1.2))

        """Настраиваем позицию окна списка наблюдения.______________________________________________________________"""
        pag.keyDown('alt')
        sleep(random.uniform(0.8, 1.2))
        pag.keyDown('v')
        sleep(random.uniform(0.4, 0.6))
        pag.keyUp('v')
        sleep(random.uniform(0.3, 0.5))
        pag.keyUp('alt')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((800, 475)), 2, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((415, 370)), 2, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((580, 513)), 30, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to(self.get_screen_position((580, 765)), 30, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((698, 375)), 2, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((850, 445)), 50, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        """Настройка окна информации._______________________________________________________________________________"""
        MouseUtils.move_to(self.get_screen_position((1700, 260)), 50, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.keyDown('t')
        sleep(random.uniform(0.4, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.3, 0.6))

        pag.keyUp('t')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((1145, 260)), 2, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((1300, 290)), 50, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((1192, 258)), 3, 3)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))
        return None

    async def custom_probes_code(self):
        pixel_x = random.randrange(7, 11)
        MouseUtils.move_to(self.get_screen_position((self.targets[0][0] + pixel_x, self.targets[0][1])), 0, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to((pag.position()[0] + 22, pag.position()[1]), 1, 7)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((1080, 398)), 10, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))
        return None

    async def custom_probes_name(self):
        pixel_x = random.randrange(7, 11)
        MouseUtils.move_to(self.get_screen_position((self.targets[0][0] + pixel_x, self.targets[0][1])), 0, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))

        MouseUtils.move_to((pag.position()[0] + 90, pag.position()[1]), 1, 7)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))
        return None

    async def close_windows_and_dock(self):
        """Закрываем настроенные окна и возвращаемся на станцию.____________________________________________________"""
        pag.keyDown('alt')
        sleep(random.uniform(0.8, 1.2))
        pag.keyDown('p')
        sleep(random.uniform(0.4, 0.6))
        pag.keyUp('p')
        sleep(random.uniform(0.3, 0.5))
        pag.keyUp('alt')
        sleep(random.uniform(0.7, 1.2))

        pag.keyDown('alt')
        sleep(random.uniform(0.8, 1.2))
        pag.keyDown('d')
        sleep(random.uniform(0.4, 0.6))
        pag.keyUp('d')
        sleep(random.uniform(0.3, 0.5))
        pag.keyUp('alt')
        sleep(random.uniform(0.7, 1.2))

        pag.keyDown('l')
        sleep(random.uniform(0.4, 0.6))
        pag.keyUp('l')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((745, 375)), 3, 3)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.3, 0.5))

        MouseUtils.move_to(self.get_screen_position((1730, 260)), 50, 2)
        sleep(random.uniform(0.3, 0.6))

        pag.keyDown('d')
        sleep(random.uniform(0.3, 0.5))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.3, 0.5))

        pag.keyUp('d')
        sleep(random.uniform(0.7, 1.2))
        return None

    async def exit_program(self):
        MouseUtils.move_to(self.get_screen_position((1350, 853)), 10, 5)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((789, 675)), 3, 3)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))

        MouseUtils.move_to(self.get_screen_position((860, 710)), 10, 5)
        sleep(random.uniform(0.3, 0.6))

        pag.mouseDown((pag.position()), button='left')
        sleep(random.uniform(0.2, 0.4))
        pag.mouseUp((pag.position()), button='left')
        sleep(random.uniform(0.7, 1.2))
        return None

    async def main(self):
        if self.state == LogicState.SCAN_START_LAUNCHER:
            await asyncio.sleep(random.uniform(1.5, 2))
            self.state = LogicState.START_LAUNCHER

        elif self.state == LogicState.START_LAUNCHER:
            task_1 = asyncio.create_task(self.move_to_target())
            await task_1
            task_2 = asyncio.create_task(self.left_click_user())
            await task_2
            task_3 = asyncio.create_task(self.click_enter())
            await asyncio.sleep(random.uniform(15, 20))
            self.state = LogicState.SCAN_START_GAME

        elif self.state == LogicState.SCAN_START_GAME:
            await asyncio.sleep(random.uniform(1.5, 2))
            self.state = LogicState.START_GAME

        elif self.state == LogicState.START_GAME:
            task_1 = asyncio.create_task(self.move_to_left_click_center_large_x())
            await asyncio.sleep(random.uniform(15, 20))
            task_2 = asyncio.create_task(self.click_alt_tab())
            await task_2
            self.state = LogicState.SCAN_LOCK_LAUNCHER

        elif self.state == LogicState.SCAN_LOCK_LAUNCHER:
            await asyncio.sleep(random.uniform(1.5, 2))
            self.state = LogicState.LOCK_LAUNCHER

        elif self.state == LogicState.LOCK_LAUNCHER:
            task_1 = asyncio.create_task(self.move_to_target())
            await task_1
            task_2 = asyncio.create_task(self.left_click_user())
            await task_2
            self.state = LogicState.STOP_LAUNCH

        # =============================================================================================================

        elif self.state == LogicState.STOP_LAUNCH:
            await asyncio.sleep(random.uniform(1.5, 2))
            self.state = LogicState.SCAN_DETECT_GIFT

        elif self.state == LogicState.SCAN_DETECT_GIFT:
            await asyncio.sleep(random.uniform(1.5, 2))
            if len(self.targets) > 0:
                self.state = LogicState.LOCK_GIFT
            else:
                self.state = LogicState.ESC_SETTINGS_GRAPHICS

        elif self.state == LogicState.LOCK_GIFT:
            task_1 = asyncio.create_task(self.success_gift())
            await task_1
            task_2 = asyncio.create_task(self.left_click_user())
            await asyncio.sleep(random.uniform(3, 4))
            self.state = LogicState.CHECK_FALSE_GIFT

        elif self.state == LogicState.CHECK_FALSE_GIFT:
            await asyncio.sleep(random.uniform(1.5, 2))
            self.state = LogicState.FINISH_LOCK_GIFT

        elif self.state == LogicState.FINISH_LOCK_GIFT:
            if len(self.targets) > 0:
                task = asyncio.create_task(self.left_click_user())
                await task
                self.state = LogicState.ESC_SETTINGS_GRAPHICS
            else:
                self.state = LogicState.ESC_SETTINGS_GRAPHICS

        elif self.state == LogicState.ESC_SETTINGS_GRAPHICS:
            task_1 = asyncio.create_task(self.click_esc())
            await task_1
            task_2 = asyncio.create_task(self.first_graphics_setup())
            await task_2
            task_3 = asyncio.create_task(self.click_esc())
            await task_3
            self.state = LogicState.START_CHAR_MAIN

        elif self.state == LogicState.START_CHAR_MAIN:
            task_1 = asyncio.create_task(self.char_select_main())
            await task_1
            task_2 = asyncio.create_task(self.left_click_user())
            await asyncio.sleep(random.uniform(15, 20))
            self.state = LogicState.START_CHAR_WINDOW

        # =============================================================================================================

        elif self.state == LogicState.START_CHAR_WINDOW:
            task_1 = asyncio.create_task(self.removes_banner())
            await task_1
            await asyncio.sleep(random.uniform(1.5, 2))
            task_2 = asyncio.create_task(self.click_esc())
            await asyncio.sleep(random.uniform(1.5, 2))
            self.state = LogicState.ESC_SETTINGS_FINAL

        elif self.state == LogicState.ESC_SETTINGS_FINAL:
            task_1 = asyncio.create_task(self.final_graphics_setup())
            await task_1
            task_2 = asyncio.create_task(self.click_esc())
            await asyncio.sleep(random.uniform(1.5, 2))
            self.state = LogicState.CUSTOM_WINDOWS

        elif self.state == LogicState.CUSTOM_WINDOWS:
            task_1 = asyncio.create_task(self.custom_windows())
            await task_1
            task_2 = asyncio.create_task(self.on_off_graphics())
            await asyncio.sleep(random.uniform(1.5, 2))
            self.state = LogicState.SCAN_UNNECESSARY_MENU_DOCK

        elif self.state == LogicState.SCAN_UNNECESSARY_MENU_DOCK:
            await asyncio.sleep(random.uniform(1.5, 2))
            self.state = LogicState.LOCK_UNNECESSARY_MENU_DOCK

        elif self.state == LogicState.LOCK_UNNECESSARY_MENU_DOCK:
            task_1 = asyncio.create_task(self.move_to_target())
            await task_1
            task_2 = asyncio.create_task(self.left_click_user())
            await task_2
            task_3 = asyncio.create_task(self.undock())
            await asyncio.sleep(random.uniform(1.5, 2))
            task_4 = asyncio.create_task(self.removes_banner())
            await asyncio.sleep(random.uniform(15, 20))
            self.state = LogicState.UNDOCK

        elif self.state == LogicState.UNDOCK:
            task = asyncio.create_task(self.ship_stop())
            await asyncio.sleep(random.uniform(1.5, 2))
            self.state = LogicState.SCAN_UNNECESSARY_MENU_SPACE

        elif self.state == LogicState.SCAN_UNNECESSARY_MENU_SPACE:
            await asyncio.sleep(random.uniform(1.5, 2))
            self.state = LogicState.LOCK_UNNECESSARY_MENU_SPACE

        elif self.state == LogicState.LOCK_UNNECESSARY_MENU_SPACE:
            task_1 = asyncio.create_task(self.move_to_target())
            await task_1
            task_2 = asyncio.create_task(self.left_click_user())
            await task_2
            task_3 = asyncio.create_task(self.on_off_graphics())
            await asyncio.sleep(random.uniform(1.5, 2))
            self.state = LogicState.CUSTOM_OVERVIEW

        elif self.state == LogicState.CUSTOM_OVERVIEW:
            task = asyncio.create_task(self.customization_overview())
            await task
            await asyncio.sleep(random.uniform(1.5, 2))
            self.state = LogicState.STEERING_CONTROL

        elif self.state == LogicState.STEERING_CONTROL:
            task = asyncio.create_task(self.steering_control())
            await task
            await asyncio.sleep(random.uniform(1.5, 2))
            self.state = LogicState.SPACE_CUSTOM_WINDOWS

        elif self.state == LogicState.SPACE_CUSTOM_WINDOWS:
            task = asyncio.create_task(self.space_custom_windows())
            await task
            self.state = LogicState.SCAN_MENU_PROBES_CODE

        elif self.state == LogicState.SCAN_MENU_PROBES_CODE:
            await asyncio.sleep(random.uniform(1.5, 2))
            self.state = LogicState.CUSTOM_MENU_PROBES_CODE

        elif self.state == LogicState.CUSTOM_MENU_PROBES_CODE:
            task = asyncio.create_task(self.custom_probes_code())
            await task
            self.state = LogicState.SCAN_MENU_PROBES_NAME

        elif self.state == LogicState.SCAN_MENU_PROBES_NAME:
            await asyncio.sleep(random.uniform(1.5, 2))
            self.state = LogicState.CUSTOM_MENU_PROBES_NAME

        elif self.state == LogicState.CUSTOM_MENU_PROBES_NAME:
            task_1 = asyncio.create_task(self.custom_probes_name())
            await task_1
            task_2 = asyncio.create_task(self.close_windows_and_dock())
            await task_2
            await asyncio.sleep(random.uniform(10, 15))
            self.state = LogicState.EXIT_PROG

        elif self.state == LogicState.EXIT_PROG:
            task_1 = asyncio.create_task(self.click_esc())
            await task_1
            task_2 = asyncio.create_task(self.exit_program())
            await task_2
            self.state = LogicState.EXIT_PROG
