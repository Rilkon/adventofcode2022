import itertools
import pathlib
import sys


def parse(parsedata):
    return [tuple(map(int, line.split(','))) for line in parsedata.splitlines()]


def part1(voxels):
    # Total surface area = 6 (sides) * number of cubes
    # Substract two from total for every pair/combination of cubes touching
    touching_cubes = sum([are_cubes_touching(cube1, cube2) * 2 for cube1, cube2 in itertools.combinations(voxels, 2)])
    return (6 * len(voxels)) - touching_cubes


def are_cubes_touching(cube_a, cube_b):
    # Two cubes are touching if "manhattan distance"(?) equals 1 (due to 1*1*1 size)
    x1, y1, z1 = cube_a
    x2, y2, z2 = cube_b
    return abs(x1 - x2) + abs(y1 - y2) + abs(z1 - z2) == 1


def part2(voxels):
    max_x = max(x for x, y, z in voxels)
    max_y = max(y for x, y, z in voxels)
    max_z = max(z for x, y, z in voxels)

    min_x = min(x for x, y, z in voxels)
    min_y = min(y for x, y, z in voxels)
    min_z = min(z for x, y, z in voxels)

    all_min = min(min_x, min_y, min_z) - 2
    all_max = max(max_x, max_y, max_z) + 2

    frontier = [[(all_min, all_min, all_min)]]
    visited = set()
    result = 0

    while frontier:
        path = frontier.pop(0)
        current = path[-1]
        x, y, z = current
        for dx, dy, dz in [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]:
            neighbor = x+dx, y+dy, z+dz
            if neighbor not in visited:
                if neighbor in voxels:
                    result += 1
                elif all((all_min <= i <= all_max) for i in neighbor):
                    visited.add(neighbor)
                    frontier.append(path + [neighbor])

    return result


def solve(puzzle_data):
    data = parse(puzzle_data)
    solution1 = part1(data)
    solution2 = part2(data)
    return solution1, solution2


if __name__ == "__main__":
    for filepath in sys.argv[1:]:
        print(f"{filepath}:")
        puzzle_input = pathlib.Path(filepath).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
