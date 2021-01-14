from hashlib import md5

data = 'qljzarfv'.encode()

diff_letters = {
    (0, -1): 'U',
    (0, 1): 'D',
    (-1, 0): 'L',
    (1, 0): 'R',
}

def is_open(path, diff):
    h = md5(data + path.encode()).hexdigest()
    return h[list(diff_letters).index(diff)] in 'bcdef'

w, h = 4, 4
start = (0, 0)
end = (w - 1, h - 1)

to_check = [start]
path_to = {start: ''}

while to_check:
    x, y = to_check.pop(0)

    if (x, y) == end:
        break

    for dx, dy in diff_letters.keys():
        nx, ny = x + dx, y + dy

        if 0 <= nx < w and 0 <= ny < h and is_open(path_to[(x, y)], (dx, dy)):
            to_check.append((nx, ny))
            path_to[(nx, ny)] = path_to[(x, y)] + diff_letters[(dx, dy)]

print(path_to[end])
