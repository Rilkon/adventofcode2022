import pathlib
import sys
import z3


def parse(parsedata):
    data = []
    for line in parsedata.splitlines():
        line = line.replace(":", "==")
        data.append(line)

    return data


def monkey_math(data, p2=False):
    s = z3.Optimize()

    # First loop, create all variables
    for exp in data:
        resultvar = exp.split("== ")[0]
        exec(f"{resultvar} = z3.Int('{resultvar}')")

    # Second loop, add expressions
    for exp in data:
        resultvar, rightside = exp.split("== ")

        # For Part 2 replace "root == x + y" with "x == y" and skip "humn = ..." because that is what we solve for
        if p2:
            if resultvar == "humn":
                continue
            if resultvar == "root":
                exp = rightside.replace("+", "==")
        exec(f"s.add({exp})")

    s.check()
    if p2:
        return s.model()[z3.Int("humn")].as_long()
    else:
        return s.model()[z3.Int("root")].as_long()


def part1(data):
    return monkey_math(data)


def part2(data):
    return monkey_math(data, True)


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
