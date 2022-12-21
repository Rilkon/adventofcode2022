import pathlib
import re
import sys
from math import prod
import mip


def parse(parsedata):
    data = []
    for line in parsedata.splitlines():
        costs = list(map(int, re.findall(r"\d+", line)))
        data.append(costs[1:])

    return data


def mip_solve(minutes, costs):
    minutes = minutes + 1
    model = mip.Model(sense=mip.MAXIMIZE)
    build_ore_robot, build_clay_robot, build_obsidian_robot, build_geode_robot = {}, {}, {}, {}
    ore, clay, obsidian, geode = {}, {}, {}, {}

    for t in range(minutes):
        ore[t] = model.add_var(var_type=mip.INTEGER, lb=0)
        clay[t] = model.add_var(var_type=mip.INTEGER, lb=0)
        obsidian[t] = model.add_var(var_type=mip.INTEGER, lb=0)
        geode[t] = model.add_var(var_type=mip.INTEGER, lb=0)

        build_ore_robot[t] = model.add_var(var_type=mip.BINARY)
        build_clay_robot[t] = model.add_var(var_type=mip.BINARY)
        build_obsidian_robot[t] = model.add_var(var_type=mip.BINARY)
        build_geode_robot[t] = model.add_var(var_type=mip.BINARY)

        model.add_constr(build_ore_robot[t] + build_clay_robot[t] + build_obsidian_robot[t] + build_geode_robot[t] <= 1)

        if t == 0:
            model.add_constr(build_ore_robot[0] == 1)
            model.add_constr(build_clay_robot[0] == 0)
            model.add_constr(build_obsidian_robot[0] == 0)
            model.add_constr(build_geode_robot[0] == 0)

            model.add_constr(ore[0] == 0)
            model.add_constr(clay[0] == 0)
            model.add_constr(obsidian[0] == 0)
            model.add_constr(geode[0] == 0)

        elif t > 0:
            spent_ore = build_ore_robot[t] * costs[0] + build_clay_robot[t] * costs[1] + \
                        build_obsidian_robot[t] * costs[2] + build_geode_robot[t] * costs[4]

            model.add_constr(spent_ore <= ore[t - 1])
            ore_robot_count = mip.quicksum(build_ore_robot[m] for m in range(minutes) if m < t)
            model.add_constr(ore[t] == ore_robot_count + ore[t - 1] - spent_ore)

            spent_clay = build_obsidian_robot[t] * costs[3]
            model.add_constr(spent_clay <= clay[t - 1])
            clay_robot_count = mip.quicksum(build_clay_robot[m] for m in range(minutes) if m < t)
            model.add_constr(clay[t] == clay_robot_count + clay[t - 1] - spent_clay)

            spent_obsidian = build_geode_robot[t] * costs[5]
            model.add_constr(spent_obsidian <= obsidian[t - 1])
            obsidian_robot_count = mip.quicksum(build_obsidian_robot[m] for m in range(minutes) if m < t)
            model.add_constr(obsidian[t] == obsidian_robot_count + obsidian[t - 1] - spent_obsidian)

            geode_robot_count = mip.quicksum(build_geode_robot[m] for m in range(minutes) if m < t)
            model.add_constr(geode[t] == geode_robot_count + geode[t - 1])

    model.objective = mip.maximize(geode[minutes - 1])
    # model.verbose = 0
    model.optimize()
    return model.objective_value


def part1(data):
    return sum([round(mip_solve(24, costs)) * (idx + 1) for idx, costs in enumerate(data)])


def part2(data):
    return prod([round(mip_solve(32, costs)) for costs in data[:3]])


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
