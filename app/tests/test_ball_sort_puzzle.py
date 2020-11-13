from modules import color
from solver import BallSortPuzzle


def test_3x3():
    data_in = [
        [color.RED, color.L_GREEN, color.RED],
        [color.L_GREEN, color.RED, color.L_GREEN],
        [],
    ]

    puzzle = BallSortPuzzle(data_in)  # type: ignore
    result = puzzle.solve()
    assert result is True

    puzzle_again = BallSortPuzzle(data_in)
    puzzle_again.play_moves(puzzle.moves)


def test_4x3():
    data_in = [
        [color.BLUE, color.ORANGE, color.BLUE, color.ORANGE],
        [color.ORANGE, color.BLUE, color.ORANGE, color.BLUE],
        [],
    ]

    puzzle = BallSortPuzzle(data_in)  # type: ignore
    result = puzzle.solve()
    assert result is True

    puzzle_again = BallSortPuzzle(data_in)
    puzzle_again.play_moves(puzzle.moves)


def test_4x5():
    data_in = [
        [color.BLUE, color.ORANGE, color.RED, color.BLUE],
        [color.ORANGE, color.ORANGE, color.RED, color.BLUE],
        [color.RED, color.BLUE, color.ORANGE, color.RED],
        [],
        [],
    ]

    puzzle = BallSortPuzzle(data_in)  # type: ignore
    result = puzzle.solve()
    assert result is True

    puzzle_again = BallSortPuzzle(data_in)
    puzzle_again.play_moves(puzzle.moves)


def test_4x7():
    data_in = [
        [color.L_GREEN, color.ORANGE, color.BLUE, color.PINK],
        [color.ORANGE, color.L_GREEN, color.BLUE, color.PINK],
        [color.PINK, color.RED, color.ORANGE, color.RED],
        [color.ORANGE, color.PINK, color.RED, color.BLUE],
        [color.L_GREEN, color.L_GREEN, color.RED, color.BLUE],
        [],
        [],
    ]

    puzzle = BallSortPuzzle(data_in)  # type: ignore
    result = puzzle.solve()
    assert result is True

    puzzle_again = BallSortPuzzle(data_in)
    puzzle_again.play_moves(puzzle.moves)


def test_4x9():
    data_in = [
        [color.PINK, color.BLUE, color.L_GREEN, color.BLUE],
        [color.ORANGE, color.GRAY, color.PINK, color.RED],
        [color.BLUE, color.L_BLUE, color.L_BLUE, color.L_GREEN],
        [color.PINK, color.ORANGE, color.ORANGE, color.L_GREEN],
        [color.GRAY, color.GRAY, color.L_GREEN, color.RED],
        [color.BLUE, color.RED, color.L_BLUE, color.L_BLUE],
        [color.RED, color.PINK, color.ORANGE, color.GRAY],
        [],
        [],
    ]

    puzzle = BallSortPuzzle(data_in)  # type: ignore
    result = puzzle.solve()
    assert result is True

    puzzle_again = BallSortPuzzle(data_in)
    puzzle_again.play_moves(puzzle.moves)


def test_4x11():
    data_in = [
        [color.RED, color.ORANGE, color.L_GREEN, color.L_BLUE],
        [color.PINK, color.VIOLET, color.GRAY, color.LIME],
        [color.L_BLUE, color.GRAY, color.L_GREEN, color.PINK],
        [color.LIME, color.ORANGE, color.ORANGE, color.L_GREEN],
        [color.RED, color.ORANGE, color.VIOLET, color.RED],
        [color.PINK, color.BLUE, color.VIOLET, color.VIOLET],
        [color.LIME, color.L_BLUE, color.BLUE, color.GRAY],
        [color.BLUE, color.RED, color.L_BLUE, color.PINK],
        [color.GRAY, color.BLUE, color.LIME, color.L_GREEN],
        [],
        [],
    ]

    puzzle = BallSortPuzzle(data_in)  # type: ignore
    result = puzzle.solve()
    assert result is True

    puzzle_again = BallSortPuzzle(data_in)
    puzzle_again.play_moves(puzzle.moves)


def test_4x14():
    data_in = [
        [color.L_BLUE, color.L_BLUE, color.GREEN, color.L_GREEN],
        [color.PINK, color.PINK, color.BLUE, color.BROWN],
        [color.LIME, color.L_GREEN, color.VIOLET, color.VIOLET],
        [color.VIOLET, color.L_GREEN, color.GRAY, color.ORANGE],
        [color.RED, color.GREEN, color.BROWN, color.ORANGE],
        [color.PINK, color.LIME, color.VIOLET, color.BLUE],
        [color.ORANGE, color.LIME, color.YELLOW, color.L_BLUE],
        [color.LIME, color.GREEN, color.RED, color.L_GREEN],
        [color.GREEN, color.YELLOW, color.GRAY, color.BLUE],
        [color.L_BLUE, color.RED, color.GRAY, color.BROWN],
        [color.ORANGE, color.YELLOW, color.PINK, color.GRAY],
        [color.YELLOW, color.RED, color.BROWN, color.BLUE],
        [],
        [],
    ]

    puzzle = BallSortPuzzle(data_in)  # type: ignore
    result = puzzle.solve()
    assert result is True

    puzzle_again = BallSortPuzzle(data_in)
    puzzle_again.play_moves(puzzle.moves)
