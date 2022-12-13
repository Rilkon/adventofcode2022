import pathlib
import sys
from ast import literal_eval
from functools import cmp_to_key
from itertools import chain


def parse(parsedata):
    return [[literal_eval(line) for line in pair.splitlines()] for pair in parsedata.strip().split("\n\n")]


def part1(data):
    return sum([idx + 1 if get_pair_diff(pair[0], pair[1]) < 0 else 0 for idx, pair in enumerate(data)])


def part2(data):
    packets = list(chain.from_iterable(pair for pair in data))
    packets.append([[2]])
    packets.append([[6]])
    packets = sorted(packets, key=cmp_to_key(get_pair_diff))
    return (packets.index([[2]]) + 1) * (packets.index([[6]]) + 1)


def get_pair_diff(left, right):
    if isinstance(left, int) and isinstance(right, int):
        return left - right
    elif isinstance(left, int) and isinstance(right, list):
        return get_pair_diff([left], right)
    elif isinstance(left, list) and isinstance(right, int):
        return get_pair_diff(left, [right])
    elif isinstance(left, list) and isinstance(right, list):
        for leftlist, rightlist in zip(left, right):
            difference = get_pair_diff(leftlist, rightlist)
            if difference:
                return difference
        return len(left) - len(right)


def solve(puzzle_data):
    data = parse(puzzle_data)
    solution1 = part1(data)
    solution2 = part2(data)
    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
