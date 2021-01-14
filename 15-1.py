data = open('15.txt').read().split('\n')

import re
from sympy.ntheory.modular import crt

disks = [re.match(r'Disc #\d+ has (\d+) positions; at time=0, it is at position (\d+).', line).groups() for line in data]
disks = [(int(x), i + int(y)) for i, (x, y) in enumerate(disks)]

c = crt(*zip(*disks))

print(c[1] - c[0] - 1)
