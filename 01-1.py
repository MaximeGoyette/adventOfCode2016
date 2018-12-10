
data = open('1.txt').read().split(', ')

data = [(x[0], int(x[1:])) for x in data]

o = (0, 0)
p = o
cd = 0
d = {
    0: (0, -1),
    1: (1, 0),
    2: (0, 1),
    3: (-1, 0)
}

def add(a, b, f):
    return (a[0] + f*b[0], a[1] + f*b[1])

for x, y in data:
    cd += {'R': 1, 'L': -1}[x]
    cd %= len(d)
    p = add(p, d[cd], y)

def manhattan_distance(a, b):
    return abs(b[0] - a[0]) + abs(b[1] - a[1])

print manhattan_distance(o, p)