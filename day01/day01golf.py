print(sorted([sum(map(int, (x.split("\n")))) for x in open("day01.txt").read().strip().split("\n\n")])[-1:][0])
print(sum(sorted([sum(map(int, (x.split("\n")))) for x in open("day01.txt").read().strip().split("\n\n")])[-3:]))

