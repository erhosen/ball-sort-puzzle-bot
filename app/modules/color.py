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
}
