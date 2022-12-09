import pathlib

import pytest

import day09 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent

moves = {(0, 2): (0, 1),
         (0, -2): (0, -1),
         (1, 2): (1, 1),
         (1, -2): (1, -1),
         (-1, 2): (-1, 1),
         (-1, -2): (-1, -1),
         (2, 0): (1, 0),
         (2, 1): (1, 1),
         (2, -1): (1, -1),
         (-2, 0): (-1, 0),
         (-2, 1): (-1, 1),
         (-2, -1): (-1, -1),
         (2, 2): (1, 1),
         (2, -2): (1, -1),
         (-2, 2): (-1, 1),
         (-2, -2): (-1, -1)}


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc.parse(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return aoc.parse(puzzle_input)


def test_get_move(example1):
    for key, value in moves.items():
        assert value == aoc.get_move(key)


def test_part1_example1(example1):
    """Test part 1 on example 1 input."""
    assert aoc.part1(example1) == 13


def test_part2_example2(example2):
    """Test part 2 on example 2 input."""
    assert aoc.part2(example2) == 36
