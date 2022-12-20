import pathlib
import sys


def parse(parsedata):
    return list(int(line) for line in parsedata.splitlines())


def part1(data):
    return mix_list(data, 1)


def mix_list(data, times):
    size = len(data)
    target = list(range(size))

    for _ in range(times):
        for idx, value in enumerate(data):
            index = target.index(idx)
            del target[index]
            target.insert(((index + value) % len(target)) - len(target), idx)

    idx_zero = target.index(data.index(0))
    return sum([data[target[(idx_zero + n) % size]] for n in [1000, 2000, 3000]])


def part2(data):
    decryption_key = 811589153
    part2data = list(int(line) * decryption_key for line in data)
    return mix_list(part2data, 10)


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
