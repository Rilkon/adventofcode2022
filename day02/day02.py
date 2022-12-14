import pathlib
import sys

# Score determination
LOSE = [["A", "Z"], ["B", "X"], ["C", "Y"]]
DRAW = [["A", "X"], ["B", "Y"], ["C", "Z"]]

POINTS = {"A": 1, "B": 2, "C": 3, "X": 1, "Y": 2, "Z": 3}

# Outcome determination
TOWIN = {"A": "Y", "B": "Z", "C": "X"}
TOLOSE = {"A": "Z", "B": "X", "C": "Y"}
TODRAW = {"A": "X", "B": "Y", "C": "Z"}


def parse(parsedata):
    return [line.split(" ") for line in parsedata.splitlines()]


def part1(data):
    return sum(get_score(pair) for pair in data)


def part2(data):
    return sum(get_score(choose_pair(pair)) for pair in data)


def choose_pair(pair: list) -> list:
    if pair[1] == "X":
        return [pair[0], TOLOSE[pair[0]]]
    elif pair[1] == "Y":
        return [pair[0], TODRAW[pair[0]]]
    else:
        return [pair[0], TOWIN[pair[0]]]


def get_score(pair: list) -> int:
    if pair in LOSE:
        return 0 + POINTS[pair[1]]
    elif pair in DRAW:
        return 3 + POINTS[pair[1]]
    else:
        return 6 + POINTS[pair[1]]


def solve(puzzle):
    data = parse(puzzle)
    solution1 = part1(data)
    solution2 = part2(data)
    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
