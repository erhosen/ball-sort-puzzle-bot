from typing import List, Optional

from color import Color
from modules import Ball


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
    def is_solved(self):
        if self.is_empty:
            return True
        if self.is_full and all(self.balls[0] == ball for ball in self.balls):
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
        if self.is_empty or self.upper_ball == ball:  # type: ignore
            return True
        return False

    def pop(self) -> Ball:
        return self.balls.pop(-1)

    def push(self, ball: Ball):
        self.balls.append(ball)

    @property
    def state(self) -> str:
        state = ''
        for i in range(self.max_size):
            try:
                state += str(self.balls[i])
            except IndexError:
                state += '#'
        return state

    def __iter__(self):
        return iter(self.balls)

    def __getitem__(self, item: int) -> Ball:
        return self.balls[item]

    def __len__(self) -> int:
        return len(self.balls)

    def __str__(self) -> str:
        return str(self.balls)
