import cv2 as cv


class Vision:
    def get_click_center(self, rectangles):
        points = []
        for (x, y, w, h) in rectangles:
            center_x = x + int(w / 2)
            center_y = y + int(h / 2)
            points.append((center_x, center_y))
        return points

    def get_click_edge_on_the_right(self, rectangles):
        points = []
        for (x, y, w, h) in rectangles:
            center_x = x + int(w - 5)
            center_y = y + int(h / 2)
            points.append((center_x, center_y))
        return points

    def draw_rectangles(self, full_img, rectangles):
        line_color = (0, 255, 0)
        line_type = cv.LINE_4
        for (x, y, w, h) in rectangles:
            top_left = (x, y)
            bottom_right = (x + w, y + h)
            cv.rectangle(full_img, top_left, bottom_right, line_color, lineType=line_type)
        return full_img

    def draw_crosshairs(self, full_img, points):
        marker_color = (255, 0, 255)
        marker_type = cv.MARKER_CROSS
        for (center_x, center_y) in points:
            cv.drawMarker(full_img, (center_x, center_y), marker_color, marker_type)
        return full_img
