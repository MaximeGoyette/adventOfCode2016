from functools import lru_cache

data = 1350

@lru_cache(None)
def is_wall(x, y):
    a = x*x + 3*x + 2*x*y + y + y*y
    a += data
    return bool(bin(a).count('1')%2)

start = (1, 1)
end = (31, 39)

to_check = [start]
seen_at = {start: 0}

while to_check:
    x, y = to_check.pop(0)

    if (x, y) == end:
        break

    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy

        if nx >= 0 and ny >= 0 and (nx, ny) not in seen_at and not is_wall(nx, ny):
            to_check.append((nx, ny))
            seen_at[(nx, ny)] = seen_at[(x, y)] + 1

print(seen_at[end])
