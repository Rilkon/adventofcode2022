# test_aoc_template.py
import pathlib
import pytest
import day06 as aoc
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
    assert example1 == "mjqjpqmgbljsphdztnvjfqwrcgsmlb"


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc.part1("mjqjpqmgbljsphdztnvjfqwrcgsmlb") == 7
    assert aoc.part1("bvwbjplbgvbhsrlpgdmjqwftvncz") == 5
    assert aoc.part1("nppdvjthqldpwncqszvftbrmjlhg") == 6
    assert aoc.part1("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg") == 10
    assert aoc.part1("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw") == 11



def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc.part2("mjqjpqmgbljsphdztnvjfqwrcgsmlb") == 19
    assert aoc.part2("bvwbjplbgvbhsrlpgdmjqwftvncz") == 23
    assert aoc.part2("nppdvjthqldpwncqszvftbrmjlhg") == 23
    assert aoc.part2("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg") == 29
    assert aoc.part2("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw") == 26


