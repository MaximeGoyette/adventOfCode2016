from hashlib import md5
from functools import lru_cache
import re

salt = 'yjdafjpo'

@lru_cache(None)
def get_hash(s: int) -> str:
    return md5((salt + str(s)).encode()).hexdigest()

i = 0

for _ in range(64):
    while True:
        i += 1

        if m := re.search(r'(.)\1{2}', get_hash(i)):
            c = m.group(1)[0]
            found = False

            for j in range(1, 1000):
                if mm := re.search(rf'({c})\1{{4}}', get_hash(i + j)):
                    found = True
                    break

            if found:
                break

print(i)
