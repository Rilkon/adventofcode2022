import copy
import pathlib
import sys
import re
import logging
from math import prod


def parse(parsedata):
    monkeys = []
    monkeydata = parsedata.splitlines()

    # Iterate in monkey blocks
    for i in range(1, len(monkeydata), 7):
        monkey_index = i // 7
        monkey_items = list(map(int, monkeydata[i].split(": ")[1].split(",")))
        monkey_operation = monkeydata[i + 1].split("Operation: new = ")[1]
        monkey_test = int(monkeydata[i + 2].split("Test: divisible by ")[1])
        monkey_true = int(monkeydata[i + 3].split("If true: throw to monkey ")[1])
        monkey_false = int(monkeydata[i + 4].split("If false: throw to monkey ")[1])

        monkey = {"index": monkey_index, "items": monkey_items, "operation": monkey_operation, "test": monkey_test,
                  "true": monkey_true, "false": monkey_false, "inspects": 0}
        monkeys.append(monkey)

    logging.debug(monkeys)
    return monkeys


def do_monkeybusiness(rounds, monkeys, part2):
    if part2:
        common_divisor = prod([monkey["test"] for monkey in monkeys])
        logging.debug(common_divisor)

    for i in range(rounds):

        for monkey in monkeys:
            logging.debug(f"Monkey {monkey['index']}: ")

            while (monkey["items"]):

                # Inspect Item
                current_item = monkey["items"].pop(0)
                monkey["inspects"] += 1
                logging.debug(f"  Monkey inspects an item with a worry level of {current_item}")

                # Perform operation by replacing 'old' with current item and eval it
                operation = monkey["operation"].replace("old", str(current_item))
                current_item = eval(operation)

                # Monkey gets bored
                if part2:
                    # Part 2 - Modulo division by the product of all monkeys test division values should keep the
                    # calculations intact while preventing worry levels from reaching 'ridiculous levels'
                    current_item = current_item % common_divisor
                else:
                    # Part 1 - Floor Divide by 3
                    current_item = current_item // 3

                # Do divisible check
                if current_item % monkey["test"] == 0:
                    monkeys[monkey["true"]]["items"].append(current_item)
                    logging.debug(f"Item with worry level {current_item} is thrown to monkey {monkey['true']}.")
                else:
                    monkeys[monkey["false"]]["items"].append(current_item)
                    logging.debug(f"Item with worry level {current_item} is thrown to monkey {monkey['false']}.")

    return monkeys


def part1(data):
    monkeys = do_monkeybusiness(20, data, False)
    return prod(sorted([monkey["inspects"] for monkey in monkeys], reverse=True)[:2])


def part2(data):
    monkeys = do_monkeybusiness(10000, data, True)
    return prod(sorted([monkey["inspects"] for monkey in monkeys], reverse=True)[:2])


def solve(puzzle_input):
    data = parse(puzzle_input)
    solution1 = part1(copy.deepcopy(data))
    solution2 = part2(copy.deepcopy(data))
    return solution1, solution2


if __name__ == "__main__":
    logging.basicConfig(stream=sys.stderr, level=logging.INFO)
    for path in sys.argv[1:]:
        logging.debug(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
