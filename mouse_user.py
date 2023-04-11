import random
import pytweening
import numpy as np
import pyautogui as pag
from pyclick import HumanCurve


class MouseUtils:
    def move_to(destination: tuple, dest_var_x=0, dest_var_y=0, **kwargs):
        # sourcery skip: use-contextlib-suppress
        """
        Use Bezier curve to simulate human-like mouse movements.
        Args:
            destination: x, y tuple of the destination point
            dest_var_x: pixel variance to add to the destination point (default 0)
            dest_var_y: pixel variance to add to the destination point (default 0)
        Kwargs:
            knotsCount: number of knots to use in the curve, higher value = more erratic movements
                        (default determined by distance)
            mouseSpeed: speed of the mouse (options: 'slowest', 'slow', 'medium', 'fast', 'fastest')
                        (default 'fast')
            tween: tweening function to use (default easeOutQuad)
        """

        offset_boundary_x = kwargs.get("offsetBoundaryX", 100)
        offset_boundary_y = kwargs.get("offsetBoundaryY", 100)
        knots_count = kwargs.get("knotsCount", MouseUtils.__calculate_knots(destination))
        distortion_mean = kwargs.get("distortionMean", 1)
        distortion_stdev = kwargs.get("distortionStdev", 1)
        distortion_frequency = kwargs.get("distortionFrequency", 0.5)
        tween = kwargs.get("tweening", pytweening.easeOutQuad)
        mouse_speed_list = ['slowest', 'slow', 'medium', 'fast', 'fastest']
        mouse_speed = kwargs.get("mouseSpeed", f"{random.choice(mouse_speed_list)}")
        mouse_speed = MouseUtils.__get_mouse_speed(mouse_speed)

        if dest_var_x > 0:
            dest_x = destination[0] + random.randrange(-dest_var_x, dest_var_x)
            dest_y = destination[1]
        elif dest_var_y > 0:
            dest_x = destination[0]
            dest_y = destination[1] + random.randrange(-dest_var_y, dest_var_y)
        elif dest_var_x > 0 and dest_var_y > 0:
            dest_x = destination[0] + random.randrange(-dest_var_x, dest_var_x)
            dest_y = destination[1] + random.randrange(-dest_var_y, dest_var_y)
        else:
            dest_x = destination[0]
            dest_y = destination[1]

        start_x, start_y = pag.position()
        for curve_x, curve_y in HumanCurve(
                (start_x, start_y),
                (dest_x, dest_y),
                offsetBoundaryX=offset_boundary_x,
                offsetBoundaryY=offset_boundary_y,
                knotsCount=knots_count,
                distortionMean=distortion_mean,
                distortionStdev=distortion_stdev,
                distortionFrequency=distortion_frequency,
                tween=tween,
                targetPoints=mouse_speed,
        ).points:
            pag.moveTo((curve_x, curve_y))
            start_x, start_y = curve_x, curve_y

    def move_rel(self, x: int, y: int, x_var: int = 100, y_var: int = 100, **kwargs):
        """
        Use Bezier curve to simulate human-like relative mouse movements.
        Args:
            x: x distance to move
            y: y distance to move
            x_var: random upper-bound pixel variance to add to the x distance (default 0)
            y_var: random upper-bound pixel variance to add to the y distance (default 0)
        Kwargs:
            knotsCount: if right-click menus are being cancelled due to erratic mouse movements,
                        try setting this value to 0.
        """
        if x_var != 0:
            x += np.random.randint(-x_var, x_var)
        if y_var != 0:
            y += np.random.randint(-y_var, y_var)
        self.move_to((pag.position()[0] + x, pag.position()[1] + y), **kwargs)

    def __calculate_knots(destination: tuple):
        """
        Calculate the knots to use in the Bezier curve based on distance.
        Args:
            destination: x, y tuple of the destination point
        """
        # calculate the distance between the start and end points
        distance = np.sqrt((destination[0] - pag.position()[0]) ** 2 + (destination[1] - pag.position()[1]) ** 2)
        res = round(distance / 200)
        return min(res, 3)

    def __get_mouse_speed(speed: str) -> int:
        """
        Converts a text speed to a numeric speed for HumanCurve (targetPoints).
        """
        if speed == "slowest":
            return random.randint(160, 185)  # (85, 100)
        elif speed == "slow":
            return random.randint(140, 165)  # (65, 80)
        elif speed == "medium":
            return random.randint(120, 145)  # (45, 60)
        elif speed == "fast":
            return random.randint(95, 125)  # (20, 40)
        elif speed == "fastest":
            return random.randint(85, 100)  # (10, 15)
        else:
            raise ValueError("Invalid mouse speed. Try 'slowest', 'slow', 'medium', 'fast', or 'fastest'.")


# MouseUtils.move_to((1000, 1000), 0, 0)
# MouseUtils.move_rel(MouseUtils, 10, 10)
