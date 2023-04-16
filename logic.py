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
    STOP_CHAR_MAIN = 13

    # INITIALIZING = 0
    # DOCK = 1
    # CUSTOM_CHAT = 2
    # SCAN_NEOCOM = 3
    # CUSTOM_NEOCOM = 4
    # SCAN_LOCK_NEOCOM = 5
    # LOCK_NEOCOM = 6
    # SCAN_UNNECESSARY_MENU = 7
    # LOCK_UNNECESSARY_MENU = 8
    # SCAN_STORAGE_WINDOW = 9
    # MOVING_WINDOW_STORAGE = 10
    # SCAN_FULL_STORAGE = 11
    # SETTINGS_STORAGE = 12
    # SCAN_LOCK_STORAGE = 13
    # LOCK_STORAGE = 14
    # SCAN_SETTINGS_STATION = 15
    # SETTINGS_STATION = 16
    # SCAN_LOCK_STATION = 17
    # LOCK_STATION = 18
    # SCAN_SETTINGS_CHAT = 19
    # SETTINGS_CHAT = 20
    # SCAN_LOCK_CHAT = 21
    # LOCK_CHAT = 22
    # UNDOCK = 100
    # STOP = 101


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

    def update_win_pos_targets(self, window_position, targets):
        self.window_position = window_position
        self.targets = targets
        return None

    """ Общие функции.=============================================================================================="""

    async def move_to_user(self):
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
        sleep(random.uniform(0.2, 0.4))
        return None

    async def move_to_left_click_center_larg_x(self):
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

    async def main(self):
        if self.state == LogicState.SCAN_START_LAUNCHER:
            await asyncio.sleep(random.uniform(1.5, 2))
            self.state = LogicState.START_LAUNCHER

        elif self.state == LogicState.START_LAUNCHER:
            task_1 = asyncio.create_task(self.move_to_user())
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
            task_1 = asyncio.create_task(self.move_to_left_click_center_larg_x())
            await asyncio.sleep(random.uniform(15, 20))
            task_2 = asyncio.create_task(self.click_alt_tab())
            await task_2
            self.state = LogicState.SCAN_LOCK_LAUNCHER

        elif self.state == LogicState.SCAN_LOCK_LAUNCHER:
            await asyncio.sleep(random.uniform(1.5, 2))
            self.state = LogicState.LOCK_LAUNCHER

        elif self.state == LogicState.LOCK_LAUNCHER:
            task_1 = asyncio.create_task(self.move_to_user())
            await task_1
            task_2 = asyncio.create_task(self.left_click_user())
            await task_2
            self.state = LogicState.STOP_LAUNCH

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
            task_2 = pag.mouseDown((pag.position()), button='left')
            await asyncio.sleep(random.uniform(0.3, 0.7))
            task_3 = pag.mouseUp((pag.position()), button='left')
            # self.state = LogicState.
