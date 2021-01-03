from modules.color import Color


class Move:
    def __init__(self, i, j, i_color: Color):
        self.i = i
        self.j = j
        self.emoji = i_color.emoji

    def __eq__(self, other: 'Move') -> bool:  # type: ignore
        return (self.i, self.j) == (other.i, other.j)

    def __repr__(self) -> str:
        return f'Ball({self})'

    def __str__(self) -> str:
        return f'{self.i} -> {self.j}'
