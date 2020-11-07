from enum import Enum
from typing import List, Optional


class Color(str, Enum):
    RED = 'R'
    GREEN = 'G'
    BLUE = 'B'
    EMPTY = ' '


class Move:
    def __init__(self, i, j):
        self.i = i
        self.j = j


class Ball:
    def __init__(self, color: Color):
        self.color = color

    @property
    def is_empty(self) -> bool:
        return self.color == Color.EMPTY

    def __repr__(self):
        return f'Ball({self})'

    def __str__(self) -> str:
        return self.color


class Flask:
    def __init__(self, num: int, column: List[Color]):
        self.num = num
        self.balls = [Ball(color) for color in column]

    @property
    def is_full(self):
        return all(not ball.is_empty for ball in self.balls)

    @property
    def is_empty(self):
        return all(ball.is_empty for ball in self.balls)

    @property
    def has_same_color(self):
        return all(self.balls[0].color == ball.color for ball in self.balls)

    @property
    def is_solved(self):
        if self.is_empty:
            return True
        if self.is_full and self.has_same_color:
            return True

        return False

    @property
    def upper_ball(self):
        for ball in self.balls:
            if ball.is_empty:
                continue
            return ball
        return ball

    def can_receive(self, ball: Ball) -> bool:
        if self.is_full:
            return False
        if self.upper_ball.is_empty or self.upper_ball.color == ball.color:
            return True
        return False

    def pop(self) -> Ball:
        upper_ball = self.upper_ball
        ball_idx = self.balls.index(upper_ball)
        self.balls[ball_idx] = Ball(Color.EMPTY)
        return upper_ball

    def push(self, ball: Ball):
        for i in range(len(self))[::-1]:
            if self.balls[i].is_empty:
                self.balls[i] = ball
                break

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
        self.flasks = [Flask(i, column) for i, column in enumerate(columns)]

    @property
    def flask_amount(self):
        return len(self.flasks)

    @property
    def flask_size(self):
        return len(self.flasks[0])

    def find_move(self) -> Optional[Move]:
        for i, flask in enumerate(self.flasks):
            upper_ball = flask.upper_ball

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

        self.commit_move(move)
        print(self)

        if self.solve():
            return True

        return False

    def __str__(self) -> str:
        result = '\n'
        for ball_idx in range(self.flask_size):
            for flask in self.flasks:
                result += f'|{flask[ball_idx]}| '
            result += '\n'
        for _ in range(self.flask_amount):
            result += ' ‾   '
        result += '\n'
        for flask in self.flasks:
            result += f' {flask.num}  '
        result += '\n'
        return result


if __name__ == "__main__":
    data_in = [
        [Color.RED, Color.GREEN, Color.RED],
        [Color.GREEN, Color.RED, Color.GREEN],
        [Color.EMPTY, Color.EMPTY, Color.EMPTY],
    ]
    solver = BallSortPuzzle(data_in)
    print(solver)
    solver.solve()
