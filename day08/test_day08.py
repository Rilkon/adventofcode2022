# test_aoc_template.py
import pathlib

import pytest

import day08 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc.parse(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return aoc.parse(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == [[3, 0, 3, 7, 3], [2, 5, 5, 1, 2], [6, 5, 3, 3, 2], [3, 3, 5, 4, 9], [3, 5, 3, 9, 0]]


def test_get_direction(example1):
    # 3 0 3 7 3
    # 2 5 5 1 2
    # 6 5 3 3 2
    # 3 3 5 4 9
    # 3 5 3 9 0
    assert aoc.get_view_dir(example1, 0, 0, "down") == [2, 6, 3, 3]
    assert aoc.get_view_dir(example1, 2, 2, "left") == [5, 6]
    assert aoc.get_view_dir(example1, 2, 2, "right") == [3, 2]
    assert aoc.get_view_dir(example1, 3, 1, "up") == [5, 5, 0]


def test_is_visible(example1):
    assert aoc.is_visible(example1, 1, 1) == 1
    assert aoc.is_visible(example1, 3, 1) == 0
    assert aoc.is_visible(example1, 2, 2) == 0
    assert aoc.is_visible(example1, 3, 3) == 0
    assert aoc.is_visible(example1, 2, 3) == 1


def test_get_viewing_distance(example1):
    # 3 0 3 7 3
    # 2 5 5 1 2
    # 6 5 3 3 2
    # 3 3 5 4 9
    # 3 5 3 9 0
    assert aoc.get_view_distance(3, aoc.get_view_dir(example1, 2, 2, "left")) == 1
    assert aoc.get_view_distance(3, aoc.get_view_dir(example1, 2, 2, "right")) == 1
    assert aoc.get_view_distance(3, aoc.get_view_dir(example1, 2, 2, "up")) == 1
    assert aoc.get_view_distance(3, aoc.get_view_dir(example1, 2, 2, "down")) == 1

    assert aoc.get_view_distance(5, aoc.get_view_dir(example1, 3, 2, "left")) == 2
    assert aoc.get_view_distance(5, aoc.get_view_dir(example1, 3, 2, "right")) == 2
    assert aoc.get_view_distance(5, aoc.get_view_dir(example1, 3, 2, "up")) == 2
    assert aoc.get_view_distance(5, aoc.get_view_dir(example1, 3, 2, "down")) == 1


def test_get_scenic_score(example1):
    assert aoc.get_scenic_score(example1, 3, 2) == 8
    assert aoc.get_scenic_score(example1, 1, 2) == 4
    assert aoc.get_scenic_score(example1, 0, 0) == 0


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc.part1(example1) == 21


def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc.part2(example1) == 8
