from pathlib import Path

import numpy as np
import pytest
from image import ImageParser
from modules import color
from solver import BallSortPuzzle

FILE_PATH = Path(__file__)


def extract_colors_from_image(image_path: Path, debug=False) -> list[list[color.Color]]:
    with open(image_path, 'rb') as f:
        file_bytes = np.asarray(bytearray(f.read()), dtype=np.uint8)
        image_parser = ImageParser(file_bytes, debug=debug)
        colors = image_parser.to_colors()

    return colors


def test_image1():
    colors = extract_colors_from_image(FILE_PATH.parent / "img/lvl_725.jpg")

    assert colors == [
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


def test_image2():
    colors = extract_colors_from_image(FILE_PATH.parent / "img/lvl_863.jpg")
    assert colors

    puzzle = BallSortPuzzle(colors)
    result = puzzle.solve()
    assert result is True


def test_image3():
    colors = extract_colors_from_image(FILE_PATH.parent / "img/lvl_1051.jpg")
    assert colors

    puzzle = BallSortPuzzle(colors)
    result = puzzle.solve()
    assert result is True


@pytest.mark.parametrize(
    'filename',
    [
        'img/lvl_5462.jpg',
        'img/lvl_10300.jpg',
        'img/lvl_5461.jpg',
    ],
)
def test_image_android(filename):
    colors = extract_colors_from_image(FILE_PATH.parent / filename)
    assert colors

    puzzle = BallSortPuzzle(colors)
    result = puzzle.solve()
    assert result is True


@pytest.mark.parametrize(
    'filename',
    [
        'img/lvl_6071.jpg',
        'img/lvl_4091.jpg',
    ],
)
def test_no_solution(filename):
    colors = extract_colors_from_image(FILE_PATH.parent / filename)
    assert colors

    puzzle = BallSortPuzzle(colors)
    result = puzzle.solve()
    assert result is False


def test_nine_flasks():
    colors = extract_colors_from_image(FILE_PATH.parent / "img/lvl_1056.jpg")
    assert colors

    puzzle = BallSortPuzzle(colors)
    result = puzzle.solve()
    assert result is True


def test_special_level_solvable():
    colors = extract_colors_from_image(FILE_PATH.parent / "img/special_level_solvable.jpg")

    assert colors == [
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

    puzzle = BallSortPuzzle(colors)
    result = puzzle.solve()
    assert result is True
    assert (
        str(puzzle.moves)
        == "[Ball(0 -> 12), Ball(0 -> 13), Ball(0 -> 12), Ball(2 -> 0), Ball(8 -> 13), Ball(2 -> 8), Ball(10 -> 0), "
        "Ball(10 -> 2), Ball(0 -> 10), Ball(0 -> 10), Ball(11 -> 12), Ball(6 -> 11), Ball(6 -> 13), Ball(3 -> 6), "
        "Ball(4 -> 3), Ball(10 -> 0), Ball(10 -> 0), Ball(10 -> 0), Ball(11 -> 10), Ball(11 -> 10), Ball(11 -> 12), "
        "Ball(3 -> 11), Ball(3 -> 11), Ball(3 -> 6), Ball(13 -> 3), Ball(13 -> 3), Ball(13 -> 3), Ball(6 -> 13), "
        "Ball(6 -> 13), Ball(6 -> 13), Ball(6 -> 2), Ball(6 -> 4), Ball(8 -> 6), Ball(8 -> 6), Ball(8 -> 6), "
        "Ball(8 -> 6), Ball(2 -> 8), Ball(2 -> 8), Ball(2 -> 8), Ball(4 -> 2), Ball(4 -> 2), Ball(1 -> 4), "
        "Ball(1 -> 13), Ball(5 -> 8), Ball(5 -> 6), Ball(7 -> 5), Ball(7 -> 11), Ball(7 -> 10), Ball(1 -> 7), "
        "Ball(1 -> 2), Ball(1 -> 12), Ball(0 -> 1), Ball(0 -> 1), Ball(0 -> 1), Ball(0 -> 1), Ball(3 -> 0), "
        "Ball(3 -> 0), Ball(3 -> 0), Ball(3 -> 0), Ball(3 -> 7), Ball(2 -> 3), Ball(2 -> 3), Ball(2 -> 3), "
        "Ball(2 -> 3), Ball(2 -> 4), Ball(5 -> 2), Ball(5 -> 2), Ball(5 -> 7), Ball(2 -> 5), Ball(2 -> 5), "
        "Ball(4 -> 2), Ball(4 -> 2), Ball(4 -> 2), Ball(4 -> 3), Ball(9 -> 2), Ball(9 -> 1), Ball(9 -> 13), "
        "Ball(7 -> 9), Ball(7 -> 9), Ball(7 -> 9), Ball(10 -> 4), Ball(9 -> 7), Ball(9 -> 7), Ball(9 -> 7), "
        "Ball(10 -> 4), Ball(7 -> 9), Ball(7 -> 9), Ball(7 -> 9), Ball(10 -> 4), Ball(9 -> 7), Ball(9 -> 7), "
        "Ball(9 -> 7), Ball(10 -> 4), Ball(5 -> 10), Ball(5 -> 10), Ball(5 -> 10), Ball(7 -> 5), Ball(5 -> 9), "
        "Ball(7 -> 5), Ball(5 -> 9), Ball(7 -> 5), Ball(5 -> 9), Ball(7 -> 5), Ball(7 -> 10), Ball(5 -> 7), "
        "Ball(9 -> 5), Ball(5 -> 7), Ball(9 -> 5), Ball(5 -> 7), Ball(9 -> 5), Ball(5 -> 7), Ball(9 -> 5), "
        "Ball(5 -> 7), Ball(9 -> 2)]"
    )


def test_special_level_unsolvable():
    colors = extract_colors_from_image(FILE_PATH.parent / "img/special_level_unsolvable.jpg")
    assert colors == [
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

    puzzle = BallSortPuzzle(colors)
    result = puzzle.solve()
    assert result is False


def test_image_and_solve():
    colors = extract_colors_from_image(FILE_PATH.parent / "img/lvl_725.jpg")
    assert colors

    puzzle = BallSortPuzzle(colors)
    result = puzzle.solve()
    assert result is True
    assert (
        str(puzzle.moves)
        == "[Ball(0 -> 12), Ball(1 -> 13), Ball(7 -> 12), Ball(11 -> 1), Ball(13 -> 11), Ball(3 -> 13), "
        "Ball(4 -> 13), Ball(9 -> 4), Ball(3 -> 9), Ball(12 -> 3), Ball(12 -> 3), Ball(4 -> 12), "
        "Ball(4 -> 12), Ball(0 -> 4), Ball(6 -> 0), Ball(11 -> 12), Ball(11 -> 12), Ball(7 -> 11), "
        "Ball(4 -> 7), Ball(4 -> 7), Ball(4 -> 11), Ball(1 -> 4), Ball(1 -> 4), Ball(5 -> 4), Ball(2 -> "
        "5), Ball(8 -> 4), Ball(5 -> 2), Ball(9 -> 8), Ball(2 -> 5), Ball(10 -> 9), Ball(1 -> 10), "
        "Ball(5 -> 2), Ball(10 -> 1), Ball(10 -> 1), Ball(2 -> 5), Ball(10 -> 6), Ball(5 -> 2), "
        "Ball(10 -> 13), Ball(2 -> 5), Ball(3 -> 10), Ball(3 -> 10), Ball(3 -> 10), Ball(2 -> 3), "
        "Ball(2 -> 10), Ball(5 -> 3), Ball(5 -> 3), Ball(2 -> 5), Ball(6 -> 2), Ball(6 -> 2), Ball(5 -> "
        "6), Ball(5 -> 6), Ball(5 -> 1), Ball(2 -> 5), Ball(2 -> 5), Ball(6 -> 2), Ball(6 -> 2), "
        "Ball(6 -> 2), Ball(6 -> 13), Ball(5 -> 6), Ball(5 -> 6), Ball(7 -> 5), Ball(7 -> 5), Ball(7 -> "
        "5), Ball(7 -> 2), Ball(6 -> 7), Ball(6 -> 7), Ball(8 -> 6), Ball(8 -> 6), Ball(7 -> 8), "
        "Ball(7 -> 8), Ball(6 -> 7), Ball(6 -> 7), Ball(8 -> 6), Ball(8 -> 6), Ball(8 -> 6), Ball(8 -> "
        "5), Ball(7 -> 8), Ball(7 -> 8), Ball(9 -> 7), Ball(7 -> 8), Ball(9 -> 7), Ball(7 -> 8), "
        "Ball(9 -> 7), Ball(9 -> 0), Ball(7 -> 9), Ball(11 -> 7), Ball(7 -> 9), Ball(11 -> 7), "
        "Ball(7 -> 9), Ball(11 -> 7), Ball(7 -> 9), Ball(11 -> 6)]"
    )
