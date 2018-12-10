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

def trace(a, b):
    if a[0] != b[0]:
        sx = 2*((b[0] - a[0]) > 0) - 1
        return [(x, a[1]) for x in xrange(a[0] + sx, b[0] + sx, sx)]
    else:
        sy = 2*((b[1] - a[1]) > 0) - 1
        return [(a[0], y) for y in xrange(a[1] + sy, b[1] + sy, sy)]

def manhattan_distance(a, b):
    return abs(b[0] - a[0]) + abs(b[1] - a[1])

visited = set([o])

for x, y in data:
    cd += {'R': 1, 'L': -1}[x]
    cd %= len(d)

    prev_p = p
    p = add(p, d[cd], y)

    for t in trace(prev_p, p):
        if t in visited:
            print manhattan_distance(t, o)
            exit(0)
        visited.add(t)