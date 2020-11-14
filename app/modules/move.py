from modules.color import COLOR_TO_EMOJI, Color


class Move:
    def __init__(self, i, j, i_color: Color):
        self.i = i
        self.j = j
        self.emoji = COLOR_TO_EMOJI[i_color]

    def __repr__(self):
        return f'Ball({self})'

    def __str__(self) -> str:
        return f'{self.i} -> {self.j}'
