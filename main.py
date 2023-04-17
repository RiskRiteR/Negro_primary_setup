import asyncio

import cv2 as cv
from time import sleep
from vision import Vision
from win_cap_detect import WindowCapture
from logic import LogicPositioning, LogicState
import pyautogui as pag


if __name__ == '__main__':

    DEBUG = False

    desktop = WindowCapture()
    logic = LogicPositioning()
    vision = Vision()
    not_targets = (0, 0)

    # while True:
    #     asyncio.run(desktop.get_position_window())
    #     logic.update_win_pos(desktop.window_rect)

    #     if logic.state == LogicState.SCAN_START_LAUNCHER:
    #         desktop.update_template('templates/start/start_launcher.png')
    #         sleep(1)
    #         asyncio.run(desktop.main())
    #         targets = vision.get_click_center(desktop.rectangles)
    #         logic.update_targets(targets)
    #         asyncio.run(logic.main())

    #     elif logic.state == LogicState.START_LAUNCHER:
    #         asyncio.run(logic.main())

    #     elif logic.state == LogicState.SCAN_START_GAME:
    #         desktop.update_template('templates/start/start_game.png')
    #         sleep(1)
    #         asyncio.run(desktop.main())
    #         targets = vision.get_click_center(desktop.rectangles)
    #         logic.update_targets(targets)
    #         asyncio.run(logic.main())

    #     elif logic.state == LogicState.START_GAME:
    #         asyncio.run(logic.main())

    #     elif logic.state == LogicState.SCAN_LOCK_LAUNCHER:
    #         desktop.update_template('templates/start/lock_launcher.png')
    #         sleep(1)
    #         asyncio.run(desktop.main())
    #         targets = vision.get_click_edge_on_the_right(desktop.rectangles)
    #         logic.update_targets(targets)
    #         asyncio.run(logic.main())

    #     elif logic.state == LogicState.LOCK_LAUNCHER:
    #         asyncio.run(logic.main())

    #     elif logic.state == LogicState.STOP_LAUNCH:
    #         asyncio.run(logic.main())
    #         cv.destroyAllWindows()
    #         break

    #     sleep(1)

    #     if desktop.screenshot is None:
    #         continue

    #     if DEBUG:
    #         debug_image = vision.draw_rectangles(desktop.screenshot, desktop.rectangles)
    #         cv.imshow('Desktop', debug_image)

    #     key = cv.waitKey(1)
    #     if key == ord("q"):
    #         cv.destroyAllWindows()
    #         break

        # ===========================================================================================================

    eve_window = WindowCapture('EVE')

    # while True:
    #     asyncio.run(eve_window.get_position_window())
    #     logic.update_win_pos(eve_window.window_rect)

    #     if logic.state == LogicState.SCAN_DETECT_GIFT:
    #         eve_window.update_template('templates/start/detect_gift.png')
    #         sleep(1)
    #         asyncio.run(eve_window.main())
    #         targets = vision.get_click_edge_on_the_right(eve_window.rectangles)
    #         logic.update_targets(targets)
    #         asyncio.run(logic.main())

    #     elif logic.state == LogicState.LOCK_GIFT:
    #         asyncio.run(logic.main())

    #     elif logic.state == LogicState.CHECK_FALSE_GIFT:
    #         eve_window.update_template('templates/start/detect_gift.png')
    #         sleep(1)
    #         asyncio.run(eve_window.main())
    #         targets = vision.get_click_edge_on_the_right(eve_window.rectangles)
    #         logic.update_targets(targets)
    #         asyncio.run(logic.main())

    #     elif logic.state == LogicState.FINISH_LOCK_GIFT:
    #         asyncio.run(logic.main())

    #     elif logic.state == LogicState.ESC_SETTINGS_GRAPHICS:
    #         asyncio.run(logic.main())

    #     elif logic.state == LogicState.START_CHAR_MAIN:
    #         asyncio.run(logic.main())
    #         cv.destroyAllWindows()
    #         break

    #     sleep(1)

    #     if eve_window.screenshot is None:
    #         continue

    #     if DEBUG:
    #         debug_image = vision.draw_rectangles(eve_window.screenshot, eve_window.rectangles)
    #         cv.imshow('EVE', debug_image)

    #     key = cv.waitKey(1)
    #     if key == ord("q"):
    #         cv.destroyAllWindows()
    #         break

        # ===========================================================================================================

    # WindowCapture.list_window_names()
    # print(pag.position())
    # exit()

    window_work = WindowCapture('EVE - Mantori Shaishi')

    while True:
        asyncio.run(window_work.get_position_window())
        logic.update_win_pos(window_work.window_rect)

        if logic.state == LogicState.START_CHAR_WINDOW:
            window_work.update_template(None)
            sleep(1)
            asyncio.run(window_work.main())
            logic.update_targets(not_targets)
            asyncio.run(logic.main())

        elif logic.state == LogicState.ESC_SETTINGS_FINAL:
            asyncio.run(logic.main())

        elif logic.state == LogicState.CUSTOM_WINDOWS:
            asyncio.run(logic.main())

        elif logic.state == LogicState.SCAN_UNNECESSARY_MENU_DOCK:
            window_work.update_template('templates/unnecessary_menu.png')
            sleep(1)
            asyncio.run(window_work.main())
            targets = vision.get_click_center(window_work.rectangles)
            logic.update_targets(targets)
            asyncio.run(logic.main())

        elif logic.state == LogicState.LOCK_UNNECESSARY_MENU_DOCK:
            asyncio.run(logic.main())

        elif logic.state == LogicState.UNDOCK:
            asyncio.run(logic.main())

        elif logic.state == LogicState.SCAN_UNNECESSARY_MENU_SPACE:
            window_work.update_template('templates/unnecessary_menu.png')
            sleep(1)
            asyncio.run(window_work.main())
            targets = vision.get_click_center(window_work.rectangles)
            logic.update_targets(targets)
            asyncio.run(logic.main())

        elif logic.state == LogicState.LOCK_UNNECESSARY_MENU_SPACE:
            asyncio.run(logic.main())

        elif logic.state == LogicState.STOP:
            cv.destroyAllWindows()
            break

        sleep(1)

        if window_work.screenshot is None:
            continue

        if DEBUG:
            debug_image = vision.draw_rectangles(window_work.screenshot, window_work.rectangles)
            cv.imshow('Window', debug_image)

        key = cv.waitKey(1)
        if key == ord("q"):
            cv.destroyAllWindows()
            break

    print("[INFO] Done.")
