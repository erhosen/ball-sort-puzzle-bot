class Color:
    def __init__(self, name):
        self.name = name

    def __repr__(self) -> str:
        return f'Color({self})'

    def __str__(self) -> str:
        return self.name


RED = Color('R')
GREEN = Color('G')
BLUE = Color('B')
