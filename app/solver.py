from typing import List, Set

from modules import Flask, Move
from modules.color import Color


class BallSortPuzzle:
    def __init__(self, columns: List[List[Color]]):
        self.flask_size = len(columns[0])  # here an assertion, that the first flask is always full
        self.flasks = [Flask(column, i, self.flask_size) for i, column in enumerate(columns)]
        self.moves: List[Move] = []
        self.states: Set[str] = set()

    def get_possible_moves(self) -> List[Move]:
        moves = []
        for flask in self.flasks:
            if flask.is_solved:
                continue

            if flask.same_three_balls:
                continue

            upper_ball = flask.upper_ball
            for potential_flask in self.flasks:
                if flask is potential_flask:
                    continue
                if potential_flask.can_receive(upper_ball):
                    moves.append(Move(flask.num, potential_flask.num, upper_ball.color))

        return moves

    def commit_move(self, move: Move) -> str:
        ball = self.flasks[move.i].pop()
        self.flasks[move.j].push(ball)
        self.moves.append(move)
        return self.calculate_state()

    def rollback_move(self, move: Move):
        ball = self.flasks[move.j].pop()
        self.flasks[move.i].push(ball)
        self.moves.pop()

    @property
    def is_solved(self):
        return all(flask.is_solved for flask in self.flasks)

    def solve(self) -> bool:
        if self.is_solved:
            return True

        for move in self.get_possible_moves():
            new_state = self.commit_move(move)
            if new_state in self.states:  # Cycle!
                self.rollback_move(move)
                continue

            self.states.add(new_state)
            if self.solve():
                return True
            self.rollback_move(move)

        return False

    def calculate_state(self) -> str:
        return '|'.join(flask.state for flask in self.flasks)

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
            result += f' {flask.num}   '
        result += '\n'
        return result


def play_moves(data_in: List[List[Color]], moves: List[Move]):
    puzzle = BallSortPuzzle(data_in)
    print(puzzle)
    for move in moves:
        print(f'## {move} ##')
        puzzle.commit_move(move)
        print(puzzle)


def _format_telegram_move(move: Move, coef: int) -> str:
    move_orig = move.i + 1  # +1 because in human world
    move_dest = move.j + 1  # count starts with 1
    if coef == 1:
        return f"\n {move_orig}th {move.emoji} -> {move_dest}th tube"

    return f'\n {move_orig}th {move.emoji * coef} -> {move_dest}th tube'


def get_telegram_repr(puzzle: BallSortPuzzle) -> str:
    assert puzzle.is_solved and puzzle.moves, "Puzzle is not solved!"

    solution = ''
    prev_move, coef = puzzle.moves[0], 1
    for move in puzzle.moves[1:]:
        if move == prev_move:
            coef += 1
        else:
            solution += _format_telegram_move(prev_move, coef)
            prev_move, coef = move, 1

    solution += _format_telegram_move(prev_move, coef)
    return f'``` {solution}```'
