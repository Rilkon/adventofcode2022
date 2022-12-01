print(sorted([sum(map(int, (x.split("\n")))) for x in open("day01.txt").read().strip().split("\n\n")], reverse=True)[0])
print(sum(sorted([sum(map(int, (x.split("\n")))) for x in open("day01.txt").read().strip().split("\n\n")], reverse=True)[0:3]))

