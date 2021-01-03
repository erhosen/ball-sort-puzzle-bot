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
    # IOS
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
    # IOS compressed
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
    # Android
    (196, 48, 60): BLUE,
    (105, 101, 100): GRAY,
    (230, 162, 87): L_BLUE,
    (149, 43, 114): VIOLET,
    (15, 152, 121): LIME,
}
