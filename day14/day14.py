import ast
import pathlib
import sys
#import matplotlib.pyplot as plt
#from matplotlib.ticker import MaxNLocator


class Reservoir:
    SOURCE = (500, 0)
    WALL = "#"
    SAND = "o"

    def __init__(self, parsedata):
        self.cave = {}
        self.y_max = 0

        for line in parsedata.splitlines():
            value_pairs = line.split(" -> ")
            for idx, element in enumerate(value_pairs):
                if idx + 1 < len(value_pairs):
                    x1, y1 = ast.literal_eval(element)
                    x2, y2 = ast.literal_eval(value_pairs[idx + 1])

                    for x in range(min(x1, x2), max(x1, x2) + 1):
                        for y in range(min(y1, y2), max(y1, y2) + 1):
                            self.cave[(x, y)] = self.WALL
                            self.y_max = max(self.y_max, y)

    def __str__(self):
        return f"Cave: {str(self.cave)}, y_max={self.y_max}"

    def get_next_spot(self, x, y):
        for pair in get_neighbors(x, y):
            if pair not in self.cave:
                return pair
        return False

    def part1(self):
        y = 0
        while y < self.y_max:
            x, y = self.SOURCE
            while y < self.y_max:
                if pair := self.get_next_spot(x, y):
                    x, y = pair
                    continue

                self.cave[(x, y)] = self.SAND
                break

        # x_values = []
        # y_values = []
        # for key, value in self.cave.items():
        #     if value == self.WALL:
        #         x_values.append(key[0])
        #         y_values.append(key[1])
        #
        # plt.scatter(x_values, y_values, marker="s", c="Black")
        # x_values = []
        # y_values = []
        # for key, value in self.cave.items():
        #     if value == self.SAND:
        #         x_values.append(key[0])
        #         y_values.append(key[1])
        # plt.scatter(x_values, y_values, marker="s", c="#C2B280")
        #
        # plt.gca().invert_yaxis()
        # plt.show()

        return sum(entry == self.SAND for entry in self.cave.values())

    def part2(self):
        while self.SOURCE not in self.cave:
            x, y = self.SOURCE
            while y < self.y_max + 1:
                if pair := self.get_next_spot(x, y):
                    x, y = pair
                    continue
                break

            self.cave[(x, y)] = self.SAND

        return sum(entry == self.SAND for entry in self.cave.values())


def get_neighbors(x, y):
    return [(a + x, y + 1) for a in [0, -1, 1]]


def solve(puzzle_data):
    reservoir = Reservoir(puzzle_data)
    solution1 = reservoir.part1()
    solution2 = reservoir.part2()
    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
