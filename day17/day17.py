import pathlib
import sys

blocknames = ["hline", "cross", "L", "vline", "square"]
blocks = [[1, 1, 1, 1],
          [[0, 1, 0], [1, 1, 1], [0, 1, 0]],
          [[0, 0, 1], [0, 0, 1], [1, 1, 1]],
          [[1], [1], [1], [1]],
          [[1, 1], [1, 1]]]
emptyline = [0, 0, 0, 0, 0, 0, 0]


def parse(parsedata):
    return list(parsedata)


def part1(data):
    print(data)

    # Each rock appears so that its left edge is two units away from the left wall and its bottom edge is three units above
    # the highest rock in the room (or the floor, if there isn't one)."

    stopped_rocks = 0
    while stopped_rocks < 2022:
        pass

        # extend play area by three + vertical_size of new rock empty rows from 1st element or floor

        # create new rock if existing one stopped falling

        # check if rock can be pushed by jet of gas
        # yes -> push in direction
        # no -> keep it

        # check if rock can fall  - else stopped_rocks++ and continue with extending playing area and new rock

        # rock falls 1 unit

    return ""


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
