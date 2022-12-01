import pathlib
import sys


def parse(parsed_input):
    # Parse input
    return parsed_input.splitlines()


def part1(elves: list) -> int:
    # Solve part 1
    return max(elves)


def part2(elves: list) -> int:
    # Solve part 2
    top_three = sorted(elves, reverse=True)[:3]
    return sum(top_three)


def get_elve_dict(calories) -> list:
    # Build list of elves along with their caloric sums
    elves = [0]
    counter = 0
    for line in calories:
        if line == "\n" or line.strip() == "":
            counter += 1
            elves.append(0)
        else:
            elves[counter] += int(line)
    return elves


def solve(puzzle_input):
    # Solve the puzzle for the given input
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
