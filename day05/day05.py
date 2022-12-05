import pathlib
import sys
from collections import deque
import re
from copy import deepcopy


def parse(crate_data, cmd_data):
    cargobay = [deque() for _ in range(int(crate_data.strip()[-1]))]
    commands = []

    # Get commandset first and ignore everything else
    for line in cmd_data.splitlines():
        if line.strip().startswith("move"):
            commands.append(list(map(int, re.findall(r"\d+", line))))

    # Reverse the direction the file is read to make building the stacks easier
    for line in reversed(crate_data.splitlines()):
        if line.strip().startswith("["):
            for i in range(0, len(line)):
                # Ignore everything except letters.
                if line[i].isalpha():
                    # Letters are always 4 spaces apart
                    # Floor division by 4 returns 0,1,2 accessing the correct stack within cargobay
                    cargobay[i // 4].append(line[i])

    return commands, cargobay


def part1(commands, cargobay, reverse=1):
    for count, source, target in commands:
        move_cargo = []
        for i in range(count):
            move_cargo.append(cargobay[source - 1].pop())
        # reverse == -1 reverses the order to avoid 99% copy paste for part2
        for cargo in move_cargo[::reverse]:
            cargobay[target - 1].append(cargo)

    return gen_result_string(cargobay)


def part2(commands, cargobay):
    return part1(commands, cargobay, -1)


def gen_result_string(cargobay):
    result = ""
    for i in range(len(cargobay)):
        if cargobay[i]:
            result += cargobay[i].pop()
    return result


def solve(puzzle):
    cms, cgbay = parse(puzzle_input[0], puzzle_input[1])
    solution1 = part1(deepcopy(cms), deepcopy(cgbay))
    solution2 = part2(deepcopy(cms), deepcopy(cgbay))
    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().split("\n\n")
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
