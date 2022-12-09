import pathlib
import sys


def parse(parsedata):
    return parsedata.splitlines()


def part1(data):
    return get_visited(data, 2)


def part2(data):
    return get_visited(data, 10)


def get_visited(data, n):
    # Generalized after part 2 to work for both parts
    knots = [(0, 0) for _ in range(n)]
    visited = set()

    for line in data:
        direction, steps = line.split(" ")
        steps = int(steps)

        for _ in range(steps):
            # Handle movement for the "head" knot (index 0)
            match direction:
                case "U":
                    knots[0] = (knots[0][0], knots[0][1] + 1)
                case "D":
                    knots[0] = (knots[0][0], knots[0][1] - 1)
                case "L":
                    knots[0] = (knots[0][0] - 1, knots[0][1])
                case "R":
                    knots[0] = (knots[0][0] + 1, knots[0][1])
                case _:
                    raise ValueError("Direction not possible")

            # After the head knot has been moved, handle the other knots
            for i in range(1, n):
                # Only move a knot if there is a relevant distance between its predecessor and itself
                if max(abs(knots[i - 1][0] - knots[i][0]), abs(knots[i - 1][1] - knots[i][1])) > 1:
                    # Determine the relative position of the current knot to its predecessor
                    rel_knot_pos = (knots[i - 1][0] - knots[i][0], knots[i - 1][1] - knots[i][1])
                    # Determine the delta and move the knot to its new position based on the delta x and y values
                    move_delta = get_move(rel_knot_pos)
                    knots[i] = (knots[i][0] + move_delta[0], knots[i][1] + move_delta[1])

            # Collect the visited position of the last knot
            visited.add(knots[n - 1])

    return len(visited)


def get_move(rel_pos):
    # This used to be a 1-1 mapping from a delta between two knots (see test_day09.py) to a new delta value
    # which is later added to the current knot to update its position.  However, it seems that the only thing that
    # really changes in that assignment is 2 => 1 and -2 => -1 hence this function to simplify
    x, y = rel_pos
    if abs(x) == 2:
        x = x // 2
    if abs(y) == 2:
        y = y // 2
    return x, y


def solve(puzzle_input):
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)
    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
