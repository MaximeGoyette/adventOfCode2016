import re

data = '''The first floor contains a hydrogen-compatible microchip and a lithium-compatible microchip.
The second floor contains a hydrogen generator.
The third floor contains a lithium generator.
The fourth floor contains nothing relevant.'''.split('\n')

#data = open('11.txt').read().split('\n')

items = {}
elevator = 1

for i, x in enumerate(data):
    m = re.findall(r'a ([\w-]+) (\w+)[,. ]', x)
    for g in m:
        items[(g[0][0] + g[1][0]).upper()] = i + 1

def draw(items, elevator):
    for i in xrange(4, 0, -1):
        line = 'F{}'.format(i).ljust(5)
        if elevator == i:
            line += 'E'.ljust(3)
        else:
            line += '.'.ljust(3)
        for item in items:
            if items[item] == i:
                line += item.ljust(3)
            else:
                line += '.'.ljust(3)
        print line
        print '-'*len(line)

draw(items, elevator)