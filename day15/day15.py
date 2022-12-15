import pathlib
import sys
import re
from z3 import *


def parse(parsedata):
    sensor_and_distance = []
    all_coords = []

    for line in parsedata.splitlines():
        x_sensor, y_sensor, x_beacon, y_beacon = map(int, re.findall(r"[\-]?[0-9]+", line))
        sensor = (x_sensor, y_sensor)
        beacon = (x_beacon, y_beacon)
        sensor_and_distance.append((x_sensor, y_sensor, manhattan_distance(sensor, beacon)))
        all_coords.append(sensor)
        all_coords.append(beacon)

    return sensor_and_distance, all_coords


def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def get_blocked_positions(sensor_and_distance, all_coords, y_pos):
    blocked = set()
    for sensor_x, sensor_y, man_dist in sensor_and_distance:
        y_dist = abs(y_pos - sensor_y)
        if y_dist <= man_dist:
            for i in range(sensor_x - (man_dist - y_dist), sensor_x + (man_dist - y_dist) + 1):
                if (i, y_pos) not in all_coords:
                    blocked.add((i, y_pos))

    return blocked


def part1(sensors, all_coords, limit):
    return len(get_blocked_positions(sensors, all_coords, limit))


def part2(sensors, limit):
    # Disclaimer:
    # Spoiled myself while researching possible approaches for part2 but this approach was too nice to ignore it
    # https://theory.stanford.edu/~nikolaj/programmingz3.html
    # https://github.com/Z3Prover/z3
    x = z3.Int("x")
    y = z3.Int("y")
    s = Solver()
    s.add(x >= 0, x < limit + 1)
    s.add(y >= 0, y < limit + 1)
    math_abs = lambda a: z3.If(a < 0, -a, a)
    for sensor_x, sensor_y, man_dist in sensors:
        # Current manhattan distance from x,y to the sensor is bigger than the manhattan distance from sensor to beacon
        # => which means it is out of range
        # The spot for which all of this is true (+ boundary conditions) should be the free spot
        s.add(math_abs(x - sensor_x) + math_abs(y - sensor_y) > man_dist)

    s.check()
    return s.model()[x].as_long() * 4000000 + s.model()[y].as_long()


def solve(puzzle_data):
    sensors, all_coords = parse(puzzle_data)
    solution1 = part1(sensors, all_coords, 2000000)
    solution2 = part2(sensors, 4000000)
    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
