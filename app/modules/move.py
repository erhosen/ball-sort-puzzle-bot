from modules.color import Color


class Move:
    def __init__(self, i, j, i_color: Color):
        self.i = i
        self.j = j
        self.emoji = i_color.emoji

    def get_telegram_repr(self) -> str:
        return f"{self.emoji} -> {self.j}"

    def __repr__(self):
        return f'Ball({self})'

    def __str__(self) -> str:
        return f'{self.i} -> {self.j}'
