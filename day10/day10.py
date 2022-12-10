import copy
import pathlib
import sys


def parse(parsedata):
    return parsedata.splitlines()[::-1]


def part1(data):
    x = 1
    cycle = 0
    signal_strength = {}

    while data:
        cycle += 1
        signal_strength[cycle] = cycle * x

        line = data.pop()

        value = 0
        command = line.split(" ")[0]
        if len(line.split(" ")) > 1:
            value = int(line.split(" ")[1])

        if command == "addx":
            data.append(f"incx {value}")
            data.append("noop")
            cycle = cycle - 1
        elif command == "incx":
            x += value

    return signal_strength[20] + signal_strength[60] + signal_strength[100] + signal_strength[140] + signal_strength[
        180] + signal_strength[220]


def part2(data):
    x = 1
    cycle = 0
    signal_strength = {}
    signals = []

    while data:
        cycle += 1
        signal_strength[cycle] = cycle * x

        line = data.pop()

        value = 0
        command = line.split(" ")[0]
        if len(line.split(" ")) > 1:
            value = int(line.split(" ")[1])

        if command == "addx":
            data.append(f"incx {value}")
            data.append("mynoop")
            cycle = cycle - 1
        elif command == "incx":
            signals = signals + [x, x]
            x += value
        elif command == "noop":
            signals = signals + [x]

        cycle += 1

    counter = 1
    for signal in signals:
        if ((counter - 1) % 40) in [signal - 1, signal, signal + 1]:
            print("#", end="")
        else:
            print(".", end="")
        if counter % 40 == 0:
            print()
        counter += 1
    print()

    return ""


def solve(puzzle_input):
    data = parse(puzzle_input)
    solution1 = part1(copy.deepcopy(data))
    solution2 = part2(copy.deepcopy(data))
    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
