import pathlib
import sys
import re
from math import cos, sin, pi
from matplotlib.patches import Polygon
import matplotlib.pyplot as plt

def parse(parsedata):
    data = []

    for line in parsedata.splitlines():
        x_sensor, y_sensor, x_beacon, y_beacon = map(int, re.findall(r"[\-]?[0-9]+", line))
        sensor = x_sensor, y_sensor
        beacon = x_beacon, y_beacon
        distance = manhattan_distance(sensor, beacon)
        data.append([*sensor, *beacon, distance])

    return data


def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def part2(data, limit):

    fig = plt.figure()

    plt.xlim([0, limit])
    plt.ylim([0, limit])

    #plt.xlim([3012781, 3012851])
    #plt.ylim([3042400, 3042498])

    for sensor_x, sensor_y, beacon_x, beacon_y, dist in data:
        currentAxis = plt.gca()

        buffer = 0.55

        polygon = Polygon([(sensor_x-dist-buffer, sensor_y),
                           (sensor_x, sensor_y-dist-buffer),
                           (sensor_x+dist+buffer, sensor_y),
                           (sensor_x, sensor_y+dist+buffer)])

        currentAxis.add_patch(polygon)

    plt.show()
    return ""


def solve(puzzle_data):
    data = parse(puzzle_data)
    solution2 = part2(data, 20)
    return solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
