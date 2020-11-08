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
