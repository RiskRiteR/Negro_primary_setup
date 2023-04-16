import asyncio
import cv2 as cv
from time import sleep
from vision import Vision
from win_cap_detect import WindowCapture
from logic import LogicPositioning, LogicState


if __name__ == '__main__':

    # WindowCapture.list_window_names()
    # print(pag.position())
    # exit()

    DEBUG = False

    desktop = WindowCapture()
    logic = LogicPositioning()
    vision = Vision()

    while True:
        if logic.state == LogicState.SCAN_START_LAUNCHER:
            desktop.update_template('templates/start/start_launcher.png')
            sleep(1)
            asyncio.run(desktop.main())
            targets = vision.get_click_center(desktop.rectangles)
            logic.update_win_pos_targets(desktop.window_rect, targets)
            asyncio.run(logic.main())

        elif logic.state == LogicState.START_LAUNCHER:
            asyncio.run(logic.main())

        elif logic.state == LogicState.SCAN_START_GAME:
            desktop.update_template('templates/start/start_game.png')
            sleep(1)
            asyncio.run(desktop.main())
            targets = vision.get_click_center(desktop.rectangles)
            logic.update_win_pos_targets(desktop.window_rect, targets)
            asyncio.run(logic.main())

        elif logic.state == LogicState.START_GAME:
            asyncio.run(logic.main())

        elif logic.state == LogicState.SCAN_LOCK_LAUNCHER:
            desktop.update_template('templates/start/lock_launcher.png')
            sleep(1)
            asyncio.run(desktop.main())
            targets = vision.get_click_edge_on_the_right(desktop.rectangles)
            logic.update_win_pos_targets(desktop.window_rect, targets)
            asyncio.run(logic.main())

        elif logic.state == LogicState.LOCK_LAUNCHER:
            asyncio.run(logic.main())

        elif logic.state == LogicState.STOP_LAUNCH:
            asyncio.run(logic.main())
            cv.destroyAllWindows()
            break

        sleep(1)

        if desktop.screenshot is None:
            continue

        if DEBUG:
            debug_image = vision.draw_rectangles(desktop.screenshot, desktop.rectangles)
            cv.imshow('Desktop', debug_image)

        key = cv.waitKey(1)
        if key == ord("q"):
            cv.destroyAllWindows()
            break

# ===================================================================================================================

    eve_window = WindowCapture('EVE')

    while True:
        if logic.state == LogicState.SCAN_DETECT_GIFT:
            eve_window.update_template('templates/start/detect_gift.png')
            sleep(1)
            asyncio.run(eve_window.main())
            targets = vision.get_click_edge_on_the_right(eve_window.rectangles)
            logic.update_win_pos_targets(eve_window.window_rect, targets)
            asyncio.run(logic.main())

        elif logic.state == LogicState.LOCK_GIFT:
            asyncio.run(logic.main())

        elif logic.state == LogicState.CHECK_FALSE_GIFT:
            eve_window.update_template('templates/start/detect_gift.png')
            sleep(1)
            asyncio.run(eve_window.main())
            targets = vision.get_click_edge_on_the_right(eve_window.rectangles)
            logic.update_win_pos_targets(eve_window.window_rect, targets)
            asyncio.run(logic.main())

        elif logic.state == LogicState.FINISH_LOCK_GIFT:
            asyncio.run(logic.main())

        elif logic.state == LogicState.ESC_SETTINGS_GRAPHICS:
            asyncio.run(logic.main())

        elif logic.state == LogicState.START_CHAR_MAIN:
            asyncio.run(logic.main())
            cv.destroyAllWindows()
            break

        sleep(1)

        if eve_window.screenshot is None:
            continue

        if DEBUG:
            debug_image = vision.draw_rectangles(eve_window.screenshot, eve_window.rectangles)
            cv.imshow('EVE', debug_image)

        key = cv.waitKey(1)
        if key == ord("q"):
            cv.destroyAllWindows()
            break

# ===================================================================================================================

    window_work = WindowCapture('EVE - Mantori Shaishi')

    while True:

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
