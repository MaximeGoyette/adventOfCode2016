a = open('3.txt').read().split('\n')
a = [map(int, (x[2:5], x[7:10], x[12:15])) for x in a]

n = 0

b = []

for y in range(0, len(a), 3):
    for x in range(3):
        b.append([a[y][x], a[y+1][x], a[y+2][x]])

for x in b:
    if x[0] + x[1] > x[2] and x[0] + x[2] > x[1] and x[1] + x[2] > x[0]:
        n += 1

print n