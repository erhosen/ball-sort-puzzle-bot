from typing import List

from modules import Ball
from modules.color import Color


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
    def has_one_color(self) -> bool:
        return all(self.balls[0] == ball for ball in self.balls)

    @property
    def is_solved(self) -> bool:
        if self.is_empty:
            return True
        if self.is_full and self.has_one_color:
            return True

        return False

    @property
    def same_three_balls(self):
        if len(self) == self.max_size - 1 and self.has_one_color:
            return True

    @property
    def upper_ball(self) -> Ball:
        assert self.balls, "Calling `upper_ball` for an empty flask!"
        return self.balls[-1]

    def can_receive(self, ball: Ball) -> bool:
        if self.is_full:
            return False
        if self.is_empty or self.upper_ball == ball:
            return True
        return False

    def pop(self) -> Ball:
        return self.balls.pop(-1)

    def push(self, ball: Ball):
        self.balls.append(ball)

    @property
    def state(self) -> str:
        state = ''.join(ball.color.symbol for ball in self.balls)
        return f"{state:#<{self.max_size}}"

    def __iter__(self):
        return iter(self.balls)

    def __getitem__(self, item: int) -> Ball:
        return self.balls[item]

    def __len__(self) -> int:
        return len(self.balls)

    def __str__(self) -> str:
        return str(self.balls)
