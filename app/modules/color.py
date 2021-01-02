class Color:
    def __init__(self, symbol, verbose_name, emoji):
        self.symbol = symbol
        self.verbose_name = verbose_name
        self.emoji = emoji

    def __repr__(self) -> str:
        return f'Color({self})'

    def __str__(self) -> str:
        return self.symbol


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
