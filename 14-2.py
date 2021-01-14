from hashlib import md5
from functools import lru_cache
import re
from progressbar import progressbar

salt = 'yjdafjpo'

@lru_cache(None)
def get_extended_hash(s: int) -> str:
    h = salt + str(s)
    for _ in range(2017):
        h = md5(h.encode()).hexdigest()
    return h

i = 0

for _ in progressbar(range(64)):
    while True:
        i += 1

        if m := re.search(r'(.)\1{2}', get_extended_hash(i)):
            c = m.group(1)[0]
            found = False

            for j in range(1, 1000):
                if mm := re.search(rf'({c})\1{{4}}', get_extended_hash(i + j)):
                    found = True
                    break

            if found:
                break

print(i)
