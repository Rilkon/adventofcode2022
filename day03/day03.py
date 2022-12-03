import pathlib
import sys


def parse(parsedata):
    return parsedata.splitlines()


def part1(data):
    priority_sum = 0
    for line in data:
        halfsize = len(line) // 2
        first, second = set(line[:halfsize]), set(line[halfsize:])
        priority_sum += get_priority(''.join(first.intersection(second)))

    return priority_sum


def part2(data):
    priority_sum = 0
    for i in range(0, len(data), 3):
        s1, s2, s3 = set(data[0+i]), set(data[1+i]), set(data[2+i])
        priority_sum += get_priority(''.join(s1.intersection(s2.intersection(s3))))

    return priority_sum


def get_priority(letter: str) -> int:
    if letter.isupper():
        # Capital A = 65 and should represent 27
        return ord(letter) - 38
    else:
        # Lowercase a = 97 and should represent 1
        return ord(letter) - 96


def solve(puzzle):
    data = parse(puzzle)
    solution1 = part1(data)
    solution2 = part2(data)
    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
