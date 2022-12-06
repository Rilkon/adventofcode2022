import pathlib
import sys


def parse(parsedata):
    return parsedata.splitlines()[0]


def part1(data):
    return find_marker(data, 4)


def part2(data):
    return find_marker(data, 14)


def find_marker(data, num_of_distinct):
    for i in range(0, len(data) - num_of_distinct - 1):
        check_set = set(data[i + x] for x in range(num_of_distinct))
        if len(check_set) == num_of_distinct:
            return i + num_of_distinct
    return 0


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
