import pathlib
import sys
from math import prod


def parse(parsedata):
    # Parse data as grid of integers
    data = [[int(x) for x in line] for line in parsedata.splitlines()]
    return data


def part1(data):
    # Result for part one is the sum of all visible trees in the grid along x and y axis
    return sum(is_visible(data, x, y) for x in range(len(data)) for y in range(len(data[0])))


def part2(data):
    # Result for part two is the product of all "scenic scores" of the trees in the grid along x and y axis
    return max(get_scenic_score(data, x, y) for x in range(len(data)) for y in range(len(data[0])))


def get_view_dir(grid, x, y, direction):
    # Helper function to get a one dimensional array from a tree at x,y in the grid representing
    # the field of view in the top/left/up/down direction
    match direction:
        case "up":
            return [grid[i][y] for i in range(x - 1, -1, -1)]
        case "down":
            return [grid[i][y] for i in range(x + 1, len(grid))]
        case "left":
            return [grid[x][i] for i in range(y - 1, -1, -1)]
        case "right":
            return [grid[x][i] for i in range(y + 1, len(grid[x]))]
        case _:
            raise ValueError(f"{direction} is not a valid direction")


def is_visible(grid, x, y):
    # Build a list of boolean values representing each of the 4 directions for a tree at x,y that is currently
    # being checked against the rest of the grid for visibility.
    # all(): A tree is considered visible from a direction if all other trees are smaller in that direction
    # any(): A tree is considered visible globally when at least one of the direction results is True
    checks = [all([height < grid[x][y] for height in get_view_dir(grid, x, y, view_dir)])
              for view_dir in ["up", "down", "left", "right"]]
    return any(checks)


def get_scenic_score(grid, x, y):
    # Build a list of viewing distances and use these as factors to calculate scenic score
    view_distances = [get_view_distance(grid[x][y], get_view_dir(grid, x, y, view_dir))
                      for view_dir in ["up", "down", "left", "right"]]
    return prod(view_distances)


def get_view_distance(curr_height, view_dir):
    # Return the viewing distance from a current height in a specific viewing direction
    for idx, height in enumerate(view_dir):
        if height >= curr_height:
            return idx + 1
    return len(view_dir)


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
