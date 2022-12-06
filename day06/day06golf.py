p1, p2, data = 4, 14, open("day06.txt").readline()
print(next(z for z in (i + p1 if (len(set(data[i + x] for x in range(p1))) == p1) else None for i in range(len(data) - p1 - 1))if z))
print(next(z for z in (i + p2 if (len(set(data[i + x] for x in range(p2))) == p2) else None for i in range(len(data) - p2 - 1))if z))
