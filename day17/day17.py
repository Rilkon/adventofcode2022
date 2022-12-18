import pathlib
import sys


def parse(parsedata):
    return list(parsedata)


def part1(jets):
    limit = 2022
    chamber = set([(x, 0) for x in range(7)])
    stopped_rocks = 0
    max_height = 0
    j = 0

    while stopped_rocks < limit:
        # Create new rock
        rock = get_rock(stopped_rocks % 5, max_height + 4)
        while True:

            # Push by jets of gas
            rock = move_rock(rock, jets[j], chamber)
            j = (j + 1) % len(jets)

            # Move rock down
            rock = move_rock(rock, "down", chamber)
            if rock & chamber:
                # Rock and chamber overlap -> undo movement and update chamber and max height
                rock = move_rock(rock, "up", chamber)
                chamber |= rock
                max_height = max([y for (x, y) in chamber])
                break

        stopped_rocks += 1
    return max_height


def get_rock(cycle, y):
    # Rock types as coordinates
    match cycle:
        case 0:
            # Hline
            return {(2, y), (3, y), (4, y), (5, y)}
        case 1:
            # Cross
            return {(3, y + 2), (2, y + 1), (3, y + 1), (4, y + 1), (3, y)}
        case 2:
            # Mirrored L
            return {(2, y), (3, y), (4, y), (4, y + 1), (4, y + 2)}
        case 3:
            # Vline
            return {(2, y), (2, y + 1), (2, y + 2), (2, y + 3)}
        case 4:
            # Square
            return {(2, y + 1), (2, y), (3, y + 1), (3, y)}

    raise ValueError(f" {cycle} not possible. Only 5 different rocks available")


def move_rock(rock, direction, chamber):
    # Return the new position of the rock after movement
    # If the rock would collide with chamber borders or with another rock, skip movement and return old position
    match direction:
        case "<":
            new_rock = {(x - 1, y) for (x, y) in rock}
            if any([x == 0 for (x, y) in rock]) or new_rock & chamber:
                return rock
            return new_rock
        case ">":
            new_rock = {(x + 1, y) for (x, y) in rock}
            if any([x == 6 for (x, y) in rock]) or new_rock & chamber:
                return rock
            return new_rock
        case "down":
            return {(x, y - 1) for (x, y) in rock}
        case "up":
            return {(x, y + 1) for (x, y) in rock}


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
