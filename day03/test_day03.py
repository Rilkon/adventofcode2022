# test_aoc_template.py
import pathlib
from webbrowser import get

import pytest
import day03 as aoc

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
    assert example1 == ["vJrwpWtwJgWrhcsFMMfFFhFp",
                        "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
                        "PmmdzqPrVvPwwTWBwg",
                        "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
                        "ttgJtRGJQctTZtZT",
                        "CrZsJsPPZsGzwwsLwLmpwMDw" ]


def test_translate_priority_lowercase():
    assert aoc.get_priority("a") == 1
    assert aoc.get_priority("c") == 3
    assert aoc.get_priority("z") == 26


def test_translate_priority_uppercase():
    assert aoc.get_priority("A") == 27
    assert aoc.get_priority("C") == 29
    assert aoc.get_priority("Z") == 52

def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc.part1(example1) == 157


def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc.part2(example1) == 70



