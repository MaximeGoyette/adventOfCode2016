a = open('1.txt').read()
a = a.split(', ')
a = [(x[0], int(x[1])) for x in a]

d = [(-1, 0), (0, 1), (1, 0), (0, -1)]
cd = 0

cc = (0, 0)

path = {cc: 0}

for x in a:
    cd += 1 if x[0] == 'R' else -1
    cd %= len(d)
    cc = (cc[0] + x[1]*d[cd][0], cc[1] + x[1]*d[cd][1])
    path[cc] = 0

def shortest_path(a, s, e, p):
    p = p if isinstance(p, list) else [p]

    if isinstance(a, dict):
        points = a
        print points
    else:
        points = {}
        for y in range(len(a)):
            for x in range(len(a[0])):
                if a[y][x] in p:
                    points[(y, x)] = 0
    
    todo = [s]
    n = 1
    while True:
        next_todo = []
        if len(todo) == 0:
            return None
        for x in todo:
            points[x] = n
            for b in [(x[0]-1, x[1]), (x[0]+1, x[1]), (x[0], x[1]-1), (x[0], x[1]+1)]:
                if points.get(b, None) == 0:
                    next_todo.append(b)
            if x == e:
                path = [e]
                while n > 0:
                    for b in [(x[0]-1, x[1]), (x[0]+1, x[1]), (x[0], x[1]-1), (x[0], x[1]+1)]:
                        if points.get(b, None) == n - 1:
                            path.append(b)
                            x = b
                    n -= 1
                return path[::-1]
        todo = next_todo
        n += 1

print shortest_path(path, (0, 0), (cc), 0)

