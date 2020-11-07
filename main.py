from enum import Enum
from typing import List


class Color(str, Enum):
    RED = 'R'
    GREEN = 'G'
    BLUE = 'B'
    EMPTY = ' '


class Ball:
    def __init__(self, color: Color):
        self.color = color

    def __str__(self) -> str:
        return f'|{self.color}|'


class Flask:
    def __init__(self, num: int, column: List[Color]):
        self.num = num
        self.balls = [Ball(color) for color in column]

    def __getitem__(self, item: int):
        return self.balls[item]

    def __len__(self):
        return len(self.balls)


class BallSortPuzzle:
    def __init__(self, columns: List[List[Color]]):
        self.flasks = [Flask(i, column) for i, column in enumerate(columns)]

    @property
    def flask_amount(self):
        return len(self.flasks)

    @property
    def flask_size(self):
        return len(self.flasks[0])

    def __str__(self) -> str:
        result = '\n'
        for ball_idx in range(self.flask_size):
            for flask in self.flasks:
                result += f'{flask[ball_idx]} '
            result += '\n'
        for _ in range(self.flask_amount):
            result += ' ‾   '
        result += '\n'
        for flask in self.flasks:
            result += f' {flask.num}  '
        return result


if __name__ == "__main__":
    data_in = [
        [Color.RED, Color.GREEN, Color.RED],
        [Color.GREEN, Color.RED, Color.GREEN],
        [Color.EMPTY, Color.EMPTY, Color.EMPTY],
    ]
    solver = BallSortPuzzle(data_in)
    print(solver)
