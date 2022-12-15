import pathlib
import sys
import re


def parse(parsedata):
    sensor_and_distance = []
    all_coords = []

    for line in parsedata.splitlines():
        numbers = map(int, re.findall(r"[\-]?[0-9]+", line))
        x_sensor, y_sensor, x_beacon, y_beacon = numbers
        sensor = (x_sensor, y_sensor)
        beacon = (x_beacon, y_beacon)
        man_dist = get_manhattan_distance(sensor, beacon)
        sensor_and_distance.append((x_sensor, y_sensor, man_dist))
        all_coords.append(sensor)
        all_coords.append(beacon)

    return sensor_and_distance, all_coords


def get_manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def get_blocked_positions(sensor_and_distance, all_coords, y_pos):

    blocked = set()
    for sensor_x, sensor_y, man_dist in sensor_and_distance:
        y_dist = abs(y_pos - sensor_y)
        if y_dist <= man_dist:
            for i in range(sensor_x - (man_dist - y_dist), sensor_x + (man_dist - y_dist) +1):
                if (i, y_pos) not in all_coords:
                    blocked.add((i, y_pos))

    return len(blocked)


def part1(sensors, all_coords):
    return get_blocked_positions(sensors, all_coords, 2000000)


def part2(sensors, all_coords):
    return ""


def solve(puzzle_data):
    sensors, all_coords = parse(puzzle_data)
    solution1 = part1(sensors, all_coords)
    solution2 = part2(sensors, all_coords)
    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
