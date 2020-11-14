class Color:
    def __init__(self, name):
        self.name = name

    def __repr__(self) -> str:
        return f'Color({self})'

    def __str__(self) -> str:
        return self.name


RED = Color('R')
GREEN = Color('G')
ORANGE = Color('O')
BLUE = Color('B')
PINK = Color('P')
VIOLET = Color('V')
LIME = Color('L')
YELLOW = Color('Y')

L_BLUE = Color('b')
L_GREEN = Color('g')

GRAY = Color('Q')
BROWN = Color('X')

RBG_TO_COLOR = {
    (134, 212, 129): L_GREEN,
    (26, 75, 119): BROWN,
    (142, 47, 104): VIOLET,
    (81, 143, 219): ORANGE,
    (187, 46, 57): BLUE,
    (224, 161, 103): L_BLUE,
    (55, 99, 46): GREEN,
    (102, 100, 99): GRAY,
    (108, 218, 236): YELLOW,
    (123, 103, 216): PINK,
    (48, 149, 127): LIME,
    (45, 57, 181): RED,
    # no compression
    (35, 43, 197): RED,
    (229, 163, 85): L_BLUE,
    (65, 140, 232): ORANGE,
    (51, 101, 17): GREEN,
    (195, 47, 59): BLUE,
    (147, 43, 114): VIOLET,
    (123, 94, 234): PINK,
    (14, 151, 120): LIME,
    (125, 214, 97): L_GREEN,
    (8, 74, 125): BROWN,
    (87, 217, 240): YELLOW,
}

RED_EMOJI = "🔴"
ORANGE_EMOJI = "🟠"
YELLOW_EMOJI = "🟡"
GREEN_EMOJI = "🟢"
BLUE_EMOJI = "🔵"
VIOLET_EMOJI = "🟣"
BROWN_EMOJI = "🟤"
L_BLUE_EMOJI = "💠"
PINK_EMOJI = "🧠"
LIME_EMOJI = "🍐"
L_GREEN_EMOJI = "🧤"
GRAY_EMOJI = "⚪"

COLOR_TO_EMOJI = {
    RED: RED_EMOJI,
    ORANGE: ORANGE_EMOJI,
    YELLOW: YELLOW_EMOJI,
    GREEN: GREEN_EMOJI,
    BLUE: BLUE_EMOJI,
    VIOLET: VIOLET_EMOJI,
    BROWN: BROWN_EMOJI,
    L_BLUE: L_BLUE_EMOJI,
    PINK: PINK_EMOJI,
    LIME: LIME_EMOJI,
    L_GREEN: L_GREEN_EMOJI,
    GRAY: GRAY_EMOJI,
}
