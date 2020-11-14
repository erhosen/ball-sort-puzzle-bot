import math
from typing import List

import cv2
import numpy as np
from modules.color import RBG_TO_COLOR, Color


def normalize(circles):
    last_y = 0
    for circle in circles:
        if math.isclose(circle[1], last_y, abs_tol=3):
            circle[1] = last_y
        else:
            last_y = circle[1]

    return circles


def img_to_colors(file_bytes):
    image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    output = image.copy()
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1.8, 20, maxRadius=40)

    ordered_colors = []
    if circles is not None:
        circles = np.round(circles[0, :]).astype("int16")
        ind = np.lexsort((circles[:, 0], circles[:, 1]))
        circles = circles[ind]
        circles = normalize(circles)
        ind = np.lexsort((circles[:, 0], circles[:, 1]))
        circles = circles[ind]
        for i, (x, y, r) in enumerate(circles):
            # cv2.circle(output, (x, y), r, (0, 255, 0), 4)
            # cv2.putText(output, str(i), (x - 5, y - 5), 1, fontScale=1, color=(0, 128, 255))
            # cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)

            rbg = output[y][x]
            color = RBG_TO_COLOR[tuple(rbg)]  # type: ignore
            ordered_colors.append(color)

    # cv2.imshow("output", output)
    # cv2.waitKey(0)

    if not ordered_colors:
        raise ValueError("Can't parse :shrug:")

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
        raise NotImplementedError()
    else:
        raise NotImplementedError()
