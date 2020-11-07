from main import BallSortPuzzle
from modules import color


def test_simple_3x3():
    data_in = [
        [color.RED, color.GREEN, color.RED],
        [color.GREEN, color.RED, color.GREEN],
        [],
    ]

    solver = BallSortPuzzle(data_in)  # type: ignore
    print(solver)
    result = solver.solve()
    assert result is True
