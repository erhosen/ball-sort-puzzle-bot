from typing import List, Optional

from modules.color import Color


class Move:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def __str__(self) -> str:
        return f'{self.i} -> {self.j}'


class Ball:
    def __init__(self, color: Color):
        self.color = color

    def __repr__(self):
        return f'Ball({self})'

    def __str__(self) -> str:
        return str(self.color)


class Flask:
    def __init__(self, column: List[Color], num: int, max_size: int):
        self.num = num
        self.balls = [Ball(color) for color in column]
        self.max_size = max_size

    @property
    def is_full(self):
        return len(self.balls) == self.max_size

    @property
    def is_empty(self) -> bool:
        return not self.balls

    @property
    def has_same_color(self):
        return all(self.balls[0].color is ball.color for ball in self.balls)

    @property
    def is_solved(self):
        if self.is_empty:
            return True
        if self.is_full and self.has_same_color:
            return True

        return False

    @property
    def upper_ball(self) -> Optional[Ball]:
        if self.balls:
            return self.balls[-1]
        return None

    def can_receive(self, ball: Ball) -> bool:
        if self.is_full:
            return False
        if not self.upper_ball or self.upper_ball.color is ball.color:
            return True
        return False

    def pop(self) -> Ball:
        return self.balls.pop(-1)

    def push(self, ball: Ball):
        self.balls.append(ball)

    def __iter__(self):
        return iter(self.balls)

    def __getitem__(self, item: int) -> Ball:
        return self.balls[item]

    def __len__(self) -> int:
        return len(self.balls)

    def __str__(self) -> str:
        return str(self.balls)


class BallSortPuzzle:
    def __init__(self, columns: List[List[Color]]):
        self.flask_amount = len(columns)
        self.flask_size = len(columns[0])
        self.flasks = [Flask(column, i, self.flask_size) for i, column in enumerate(columns)]

    def find_move(self) -> Optional[Move]:
        for i, flask in enumerate(self.flasks):
            upper_ball = flask.upper_ball
            if not upper_ball:
                continue

            for j, potential_flask in enumerate(self.flasks):
                if i == j:
                    continue
                if potential_flask.can_receive(upper_ball):
                    return Move(i, j)
        return None

    def commit_move(self, move: Move):
        ball = self.flasks[move.i].pop()
        self.flasks[move.j].push(ball)

    @property
    def is_solved(self):
        return all(flask.is_solved for flask in self.flasks)

    def solve(self) -> bool:
        if self.is_solved:
            return True

        move = self.find_move()
        if not move:
            return False

        print(f'## {move} ##')
        self.commit_move(move)
        print(self)

        if self.solve():
            return True

        return False

    def __str__(self) -> str:
        result = '\n'
        for ball_idx in range(self.flask_size - 1, -1, -1):
            for flask in self.flasks:
                try:
                    ball = flask[ball_idx]
                except IndexError:
                    ball = ' '  # type: ignore
                result += f'|{ball}| '
            result += '\n'
        for flask in self.flasks:
            result += f' {flask.num}  '
        result += '\n'
        return result
