import math
from collections import Counter
from typing import Any, List

import cv2
import numpy as np
from modules.color import Color, get_closest_color


class ImageParserError(Exception):
    pass


class ImageParser:
    def __init__(self, file_bytes: np.ndarray, debug=False):
        self.image_orig = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
        self.image_cropped = self.get_cropped_image(self.image_orig)

        self.debug = debug

    @staticmethod
    def get_cropped_image(image):
        height, width, _ = image.shape
        quarter = int(height / 4)
        cropped_img = image[quarter : height - quarter]
        return cropped_img

    @staticmethod
    def normalize_circles(circles):
        last_y = 0
        for circle in circles:
            if math.isclose(circle[1], last_y, abs_tol=3):
                circle[1] = last_y
            else:
                last_y = circle[1]
        return circles

    @staticmethod
    def get_dominant_color(circle) -> Color:
        colors, count = np.unique(circle.reshape(-1, circle.shape[-1]), axis=0, return_counts=True)
        dominant = colors[count.argmax()]
        return get_closest_color(dominant)

    @staticmethod
    def consistency_check(ordered_colors):
        counter = Counter(ordered_colors)
        if not all(count == 4 for count in counter.values()):
            raise ImageParserError(f"Inconsistent number of colors: {counter}")

    @staticmethod
    def fit_colors_to_flasks(ordered_colors, flasks_line1: int, flasks_line2: int) -> List[List[Color]]:
        balls_line1 = flasks_line1 * 4
        line1: List[List[Color]] = [[] for _ in range(flasks_line1)]
        for i, color in enumerate(reversed(ordered_colors[:balls_line1])):
            line1[i % flasks_line1].append(color)
        line1.reverse()

        line2: List[List[Color]] = [[] for _ in range(flasks_line2)]
        for j, color in enumerate(reversed(ordered_colors[balls_line1:])):
            line2[j % flasks_line2].append(color)
        line2.reverse()

        return line1 + line2 + [[], []]

    def get_normalized_circles(self) -> List[Any]:
        image_cropped_gray = cv2.cvtColor(self.image_cropped, cv2.COLOR_BGR2GRAY)
        circles = cv2.HoughCircles(image_cropped_gray, cv2.HOUGH_GRADIENT, 2, 20, maxRadius=27)
        if circles is None:
            raise ImageParserError("No circles :shrug:")

        circles = np.round(circles[0, :]).astype("int16")
        ind = np.lexsort((circles[:, 0], circles[:, 1]))
        circles = circles[ind]
        circles = self.normalize_circles(circles)
        ind = np.lexsort((circles[:, 0], circles[:, 1]))
        circles = circles[ind]
        return circles

    def to_colors(self) -> List[List[Color]]:
        normalized_circles = self.get_normalized_circles()
        ordered_colors = []
        for i, (x, y, r) in enumerate(normalized_circles):
            small_r = r - 3
            circle = self.image_cropped[y - small_r : y + small_r, x - small_r : x + small_r]
            if self.debug:
                cv2.imwrite(f"img/img_{i}.jpg", circle)
            color = self.get_dominant_color(circle)
            ordered_colors.append(color)

        self.consistency_check(ordered_colors)

        if len(ordered_colors) == 48:
            return self.fit_colors_to_flasks(ordered_colors, flasks_line1=7, flasks_line2=5)
        elif len(ordered_colors) == 36:
            return self.fit_colors_to_flasks(ordered_colors, flasks_line1=6, flasks_line2=3)
        else:
            raise ImageParserError("NotImplementedError")
