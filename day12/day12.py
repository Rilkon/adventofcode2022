import itertools
import pathlib
import sys

import matplotlib.pyplot as plt


def parse(parsedata):
    # Parse input as a 2d grid consisting of the integer values of a-z as height levels
    # Remember start and goal
    start, goal = (0, 0)
    grid = [[0 for _ in line] for line in parsedata.splitlines()]
    for i, row in enumerate(parsedata.splitlines()):
        for j, col in enumerate(row):
            if row[j] == "S":
                grid[i][j] = ord("a")
                start = (i, j)
            elif row[j] == "E":
                grid[i][j] = ord("z")
                goal = (i, j)
            else:
                grid[i][j] = ord(row[j])

    return grid, start, goal


def part1_and_2(grid, start, goal, plot=False):
    # Part 1 - Start to Goal as described
    route = astar(grid, start, goal)

    # Option to plot the route
    if plot:
        plot_path(grid, start, goal, route[::-1])

    # Part 1: Length from start to goal
    # Part 2: Length of shortest route which arrives at value of a from goal
    return len(route), len(list(itertools.takewhile(lambda x: grid[x[0]][x[1]] != ord("a"), route[1:])))


def find_elements(grid, element):
    result = []
    for i, e in enumerate(grid):
        try:
            result.append((i, e.index(element)))
        except ValueError:
            pass
    if len(result) > 0:
        return result
    raise ValueError(f"{element} is not in list")


def heuristic(a, b):
    # Manhattan distance because movement is always horizontal or vertical?
    return abs((b[0] - a[0]) + abs(b[1] - a[1]))


def astar(array, start, goal):
    closed_set = set()
    came_from = {}
    f_score = {start: heuristic(start, goal)}
    g_score = {start: 0}
    open_set = [(f_score[start], start)]
    # no diagonal movement allowed, only 4 possible neighbors
    neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while open_set:

        current = open_set.pop(0)[1]
        if current == goal:

            total_path = []
            while current in came_from:
                total_path.append(current)
                current = came_from[current]

            return total_path

        closed_set.add(current)

        for x, y in neighbors:

            neighbor = current[0] + x, current[1] + y
            tentative_g_score = g_score[current] + heuristic(current, neighbor)

            if 0 > neighbor[0] or neighbor[0] >= len(array):
                # x border
                continue
            if 0 > neighbor[1] or neighbor[1] >= len(array[0]):
                # y border
                continue
            if array[neighbor[0]][neighbor[1]] - array[current[0]][current[1]] > 1:
                # Difference between current element and next element is > 1 (no climbing allowed)
                continue
            if neighbor in closed_set:
                # already done
                continue

            if tentative_g_score < g_score.get(neighbor, 0) or neighbor not in [i[1] for i in open_set]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                open_set.append((f_score[neighbor], neighbor))

    return False


def plot_path(grid, start, goal, route):
    x_coords = []
    y_coords = []

    for i in (range(0, len(route))):
        x = route[i][0]
        y = route[i][1]

        x_coords.append(x)
        y_coords.append(y)

    fig, ax = plt.subplots(figsize=(20, 20))
    ax.imshow(grid, cmap=plt.cm.Dark2)
    ax.scatter(start[1], start[0], marker="*", color="yellow", s=200)
    ax.scatter(goal[1], goal[0], marker="*", color="red", s=200)
    ax.plot(y_coords, x_coords, color="black")

    plt.show()


def solve(puzzle_data):
    data, start, goal = parse(puzzle_data)
    solution1, solution2 = part1_and_2(data, start, goal, False)
    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
