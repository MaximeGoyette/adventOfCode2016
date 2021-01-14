from hashlib import md5
from functools import lru_cache
from itertools import product

data = 'ihgpwlah'.encode()

moves_diff = {
    'U': (0, -1),
    'D': (0, 1),
    'L': (-1, 0),
    'R': (1, 0),
}

@lru_cache(None)
def validate_path(path):
    x, y = 0, 0

    for i in range(1, len(path)):
        h = md5(data + path[:i].encode()).hexdigest()

        if h[list(moves_diff).index(move)] not in 'bcdef':
            return False

        dx, dy = moves_diff[move]
        nx, ny = x + dx, y + dy

        if not (0 <= nx < 4 and 0 <= ny < 4):
            return False

        x, y = nx, ny

    return True


valid_paths = []

while True:
    valid_moves = []

    for path in product(*valid_paths):
        for move in 'UDLR':
            if validate_path(''.join(path + (move,))):
                valid_moves.append(move)

    if not valid_moves:
        break

    valid_paths.append(valid_moves)

print(valid_paths)
