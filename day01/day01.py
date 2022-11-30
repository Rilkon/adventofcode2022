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


if __name__ == "__main__":
    path = input("Path: ")
    print(f"\n{path}:")

    puzzle_input = pathlib.Path(path).read_text().strip()
    numbers = parse(puzzle_input)

    print(part1(numbers))
