import pathlib

def parse(puzzle_input):
    # Parse input.
    return [int(line) for line in puzzle_input.split()]


def part1(numbers):
    """Solve part 1."""
    for num1 in numbers:
        for num2 in numbers:
            if num1 < num2 and num1 + num2 == 2020:
                return num1 * num2

def part2(numbers):
    return 0

def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)
    return solution1, solution2


if __name__ == "__main__":
    path = "./day01.txt"
    puzzle_input = pathlib.Path(path).read_text().strip()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
