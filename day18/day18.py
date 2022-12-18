import itertools
import pathlib
import sys


def parse(parsedata):
    return [tuple(map(int, line.split(','))) for line in parsedata.splitlines()]


def are_cubes_touching(cube_a, cube_b):
    # Two cubes are touching if "manhattan distance"(?) equals 1 (due to 1*1*1 size)
    x1, y1, z1 = cube_a
    x2, y2, z2 = cube_b
    return abs(x1 - x2) + abs(y1 - y2) + abs(z1 - z2) == 1


def part1(data):
    # Substract two from our result for every pair/combination of cubes touching
    result = sum([are_cubes_touching(cube1, cube2) * 2 for cube1, cube2 in itertools.combinations(data, 2)])
    return (6 * len(data)) - result


def part2(data):
    return ""


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
