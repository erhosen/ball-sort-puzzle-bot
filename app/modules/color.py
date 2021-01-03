import numpy as np


class Color:
    def __init__(self, symbol, verbose_name, emoji):
        self.symbol = symbol
        self.verbose_name = verbose_name
        self.emoji = emoji

    def __repr__(self) -> str:
        return f'Color({self})'

    def __str__(self) -> str:
        return self.emoji


RED = Color('R', 'Red', '🔴')
GREEN = Color('G', 'Green', '🟢')
ORANGE = Color('O', 'Orange', '🟠')
BLUE = Color('B', 'Blue', '🔵')
PINK = Color('P', 'Pink', '🧠')
VIOLET = Color('V', 'Violet', '🟣')
LIME = Color('L', 'Lime', '🍐')
YELLOW = Color('Y', 'Yellow', '🟡')

L_BLUE = Color('b', 'Light Blue', '💠')
L_GREEN = Color('g', 'Light Green', '🧤')

GRAY = Color('Q', 'Gray', '⚪')
BROWN = Color('X', 'Brown', '🟤')

RBG_TO_COLOR = {
    (147, 42, 115): VIOLET,
    (8, 74, 125): BROWN,
    (229, 163, 85): L_BLUE,
    (68, 140, 234): ORANGE,
    (196, 46, 59): BLUE,
    (51, 100, 18): GREEN,
    (35, 43, 197): RED,
    (87, 216, 241): YELLOW,
    (125, 214, 97): L_GREEN,
    (123, 94, 234): PINK,
    (16, 150, 120): LIME,
    (102, 100, 99): GRAY,
}
COLORS = np.array(list(RBG_TO_COLOR.keys()))


def get_closest_color(color: np.ndarray) -> Color:
    distances = np.sqrt(np.sum((COLORS - color) ** 2, axis=1))
    index_of_smallest = np.where(distances == np.amin(distances))
    smallest_distance = COLORS[index_of_smallest].flat
    return RBG_TO_COLOR[tuple(smallest_distance)]  # type: ignore
