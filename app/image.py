import math
from typing import List

import cv2
import numpy as np
from modules.color import RBG_TO_COLOR, Color


class ImageParsingError(Exception):
    pass


def normalize(circles):
    last_y = 0
    for circle in circles:
        if math.isclose(circle[1], last_y, abs_tol=3):
            circle[1] = last_y
        else:
            last_y = circle[1]

    return circles


def get_dominant_color(circle) -> Color:
    colors, count = np.unique(circle.reshape(-1, circle.shape[-1]), axis=0, return_counts=True)
    dominant = tuple(colors[count.argmax()])
    try:
        return RBG_TO_COLOR[dominant]  # type: ignore
    except KeyError:
        raise ImageParsingError(f"Unexpected color {dominant}")


def get_cropped_image(image):
    height, width, _ = image.shape
    quarter = int(height / 4)
    cropped_img = image[quarter : height - quarter]
    return cropped_img


def img_to_colors(file_bytes):
    image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    image = get_cropped_image(image)
    img_copy = image.copy()
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    circles = cv2.HoughCircles(gray_image, cv2.HOUGH_GRADIENT, 2, 20, maxRadius=27)

    ordered_colors = []
    if circles is not None:
        circles = np.round(circles[0, :]).astype("int16")
        ind = np.lexsort((circles[:, 0], circles[:, 1]))
        circles = circles[ind]
        circles = normalize(circles)
        ind = np.lexsort((circles[:, 0], circles[:, 1]))
        circles = circles[ind]
        for i, (x, y, r) in enumerate(circles):
            small_r = r - 3
            crop = img_copy[y - small_r : y + small_r, x - small_r : x + small_r]
            color = get_dominant_color(crop)
            ordered_colors.append(color)

            # cv2.imwrite(f"/Users/vviazovetskov/PycharmProjects/ball-sort-puzzle/app/tests/img/img_{i}.jpg", crop)  # noqa
            # cv2.circle(img_copy, (x, y), r, (0, 255, 0), 4)
            # cv2.putText(img_copy, str(i), (x - 5, y - 5), 1, fontScale=1, color=(0, 128, 255))
            # cv2.rectangle(img_copy, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)

    # cv2.imshow("output", img_copy)
    # cv2.waitKey(0)

    if not ordered_colors:
        raise ImageParsingError("No circles :shrug:")

    if len(ordered_colors) == 48:
        flasks1: List[List[Color]] = [[] for _ in range(7)]
        for i, color in enumerate(reversed(ordered_colors[:28])):
            flasks1[i % 7].append(color)
        flasks1.reverse()

        flasks2: List[List[Color]] = [[] for _ in range(5)]
        for j, color in enumerate(reversed(ordered_colors[28:])):
            flasks2[j % 5].append(color)
        flasks2.reverse()

        return flasks1 + flasks2 + [[], []]
    elif len(ordered_colors) == 36:
        raise ImageParsingError("NotImplementedError")
    else:
        raise ImageParsingError("NotImplementedError")
