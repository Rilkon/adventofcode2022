import pathlib
import sys


def parse(puzzle_input):
    # Parse input
    return puzzle_input.splitlines()


def part1(elves):
    # Solve part 1
    return elves[max(elves, key=elves.get)]


def part2(elves):
    # Solve part 2
    top_three = sorted(elves, key=elves.get, reverse=True)[:3]
    return sum([elves[value] for value in top_three])


def get_elve_dict(calories) -> dict:
    # build dictionary of elves along with their caloric sums
    elves = {}
    counter = 1
    for line in calories:

        if line == "\n" or line.strip() == "":
            counter += 1
        else:
            if counter in elves.keys():
                elves[counter] = elves[counter] + int(line)
            else:
                elves[counter] = int(line)

    return elves


def solve(puzzle_input):
    # solve the puzzle for the given input
    data = parse(puzzle_input)
    elves = get_elve_dict(data)
    solution1 = part1(elves)
    solution2 = part2(elves)
    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
