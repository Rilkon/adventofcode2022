import pathlib
import sys
import re


def parse(parsedata):
    return parsedata.splitlines()


def part1(data):

    counter = 0
    for line in data:
        one_min, one_max, two_min, two_max = map(int, re.findall(r"\d+", line))
        if (one_min < two_min or one_max > two_max) and (two_min < one_min or two_max > one_max):
            counter += 1

    return counter

def part2(data):
    counter = 0
    for line in data:
        one_min, one_max, two_min, two_max = map(int, re.findall(r"\d+", line))
        if (two_min <= one_min <= two_max) or (one_min <= two_min <= one_max):
            counter += 1

    return counter



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
