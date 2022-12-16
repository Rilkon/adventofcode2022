import pathlib
import re
import sys
import heapq


def parse(parsedata):
    flows = {}
    tunnels = {}
    for line in parsedata.splitlines():
        name, flow, paths = re.findall \
            (r"Valve ([A-Z]+) has flow rate=([0-9]+); tunnel(?:s)? lead(?:s)? to valve(?:s)? (.*)$", line)[0]
        flows[name] = int(flow)
        tunnels[name] = paths.split(", ")

    return tunnels, flows


def best_scoring_path(tunnels, flows, p2=False):
    # Score, Valve, Minute, Opened Valves as set
    frontier = [(0, "AA", 1, set())]
    # Heapify the frontier https://docs.python.org/3/library/heapq.html
    # Should in theory prioritze the value with the highest score when popping element
    heapq.heapify(frontier)
    # (Current_Location, Minute): Score
    visited = {}
    best_score = 0
    limit = 26 if p2 else 30

    while frontier:
        score, current_valve, minute, open_valves = heapq.heappop(frontier)

        # Each time the limit is reached, save the current maximum as best score
        if minute == limit:
            best_score = max(best_score, score)
            continue

        # Prevent key error and make sure comparison is false by -1 default value
        if visited.get((current_valve, minute), -1) >= score:
            continue
        visited[(current_valve, minute)] = score

        # For unopened valves with positive flow calculate the new state including that valve being open
        # Push the new state to the frontier and remove the open valve from the current iteration again
        if flows[current_valve] > 0 and current_valve not in open_valves:
            open_valves.add(current_valve)
            new_score = score + sum(flows[valve] for valve in open_valves)
            heapq.heappush(frontier, (new_score, current_valve, minute + 1, set(open_valves)))
            open_valves.discard(current_valve)

        # Valve was not opened. Calculcate the new score based on the currently open valves and a new state for
        # each possible tunnel to explore from current valve
        new_score = score + sum(flows[valve] for valve in open_valves)
        for tunnel in tunnels[current_valve]:
            heapq.heappush(frontier, (new_score, tunnel, minute + 1, set(open_valves)))

    return best_score


def part1(tunnels, flows):
    return best_scoring_path(tunnels, flows)


def part2(tunnels, flows):
    return best_scoring_path(tunnels, flows, True)


def solve(puzzle_data):
    d1, d2 = parse(puzzle_data)
    solution1 = part1(d1, d2)
    solution2 = part2(d1, d2)
    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
