from modules import color
from solver import BallSortPuzzle, play_moves


def test_3x3():
    data_in = [
        [color.RED, color.GREEN, color.RED],
        [color.GREEN, color.RED, color.GREEN],
        [],
    ]

    puzzle = BallSortPuzzle(data_in)
    result = puzzle.solve()
    assert result is True
    play_moves(data_in, puzzle.moves)


def test_4x3():
    data_in = [
        [color.BLUE, color.ORANGE, color.BLUE, color.ORANGE],
        [color.ORANGE, color.BLUE, color.ORANGE, color.BLUE],
        [],
    ]

    puzzle = BallSortPuzzle(data_in)
    result = puzzle.solve()
    assert result is True
    play_moves(data_in, puzzle.moves)


def test_4x5():
    data_in = [
        [color.BLUE, color.ORANGE, color.RED, color.BLUE],
        [color.ORANGE, color.ORANGE, color.RED, color.BLUE],
        [color.RED, color.BLUE, color.ORANGE, color.RED],
        [],
        [],
    ]

    puzzle = BallSortPuzzle(data_in)
    result = puzzle.solve()
    assert result is True
    play_moves(data_in, puzzle.moves)


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

    puzzle = BallSortPuzzle(data_in)
    result = puzzle.solve()
    assert result is True
    play_moves(data_in, puzzle.moves)


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

    puzzle = BallSortPuzzle(data_in)
    result = puzzle.solve()
    assert result is True
    play_moves(data_in, puzzle.moves)


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

    puzzle = BallSortPuzzle(data_in)
    result = puzzle.solve()
    assert result is True
    play_moves(data_in, puzzle.moves)


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

    puzzle = BallSortPuzzle(data_in)
    result = puzzle.solve()
    assert result is True
    play_moves(data_in, puzzle.moves)


def test_5x14_solvable():
    data_in = [
        [color.GREEN, color.PINK, color.BROWN, color.GREEN, color.BROWN],
        [color.BROWN, color.YELLOW, color.BLUE, color.VIOLET, color.GRAY],
        [color.GRAY, color.YELLOW, color.L_GREEN, color.L_BLUE, color.PINK],
        [color.BLUE, color.GREEN, color.VIOLET, color.LIME, color.VIOLET],
        [color.RED, color.YELLOW, color.GRAY, color.YELLOW, color.LIME],
        [color.ORANGE, color.BLUE, color.ORANGE, color.L_BLUE, color.L_GREEN],
        [color.YELLOW, color.L_GREEN, color.VIOLET, color.GREEN, color.RED],
        [color.ORANGE, color.BLUE, color.RED, color.LIME, color.ORANGE],
        [color.L_GREEN, color.L_BLUE, color.L_BLUE, color.L_BLUE, color.GREEN],
        [color.GRAY, color.BLUE, color.VIOLET, color.PINK, color.GRAY],
        [color.ORANGE, color.RED, color.PINK, color.L_GREEN, color.PINK],
        [color.LIME, color.LIME, color.BROWN, color.RED, color.BROWN],
        [],
        [],
    ]

    puzzle = BallSortPuzzle(data_in)
    result = puzzle.solve()
    assert result is True
    play_moves(data_in, puzzle.moves)


def test_5x14_no_solution():
    data_in = [
        [color.L_BLUE, color.GRAY, color.BROWN, color.YELLOW, color.LIME],
        [color.LIME, color.BROWN, color.L_GREEN, color.GREEN, color.PINK],
        [color.L_GREEN, color.YELLOW, color.L_GREEN, color.VIOLET, color.L_BLUE],
        [color.RED, color.BROWN, color.GREEN, color.BLUE, color.LIME],
        [color.VIOLET, color.ORANGE, color.ORANGE, color.YELLOW, color.L_BLUE],
        [color.GRAY, color.GRAY, color.ORANGE, color.VIOLET, color.VIOLET],
        [color.RED, color.ORANGE, color.L_GREEN, color.VIOLET, color.RED],
        [color.L_BLUE, color.L_BLUE, color.L_GREEN, color.BLUE, color.ORANGE],
        [color.RED, color.YELLOW, color.PINK, color.LIME, color.GREEN],
        [color.RED, color.GREEN, color.YELLOW, color.BLUE, color.GREEN],
        [color.PINK, color.LIME, color.PINK, color.BLUE, color.GRAY],
        [color.GRAY, color.BROWN, color.BROWN, color.BLUE, color.PINK],
        [],
        [],
    ]

    puzzle = BallSortPuzzle(data_in)
    result = puzzle.solve()
    assert result is False
    play_moves(data_in, puzzle.moves)
