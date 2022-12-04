import re
data = [list(map(int, re.findall("\d+", line))) for line in open("day04.txt")]
print(sum((a >= x and b <= y) or (x >= a and y <= b) for a, b, x, y in data))
print(sum((x <= a <= y) or (a <= x <= b) for a, b, x, y in data))