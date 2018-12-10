import re

data = open('8.txt').read().split('\n')

screen = [['.' for _ in xrange(50)] for _ in xrange(6)]

def rect(screen, A, B):
    for y in xrange(B):
        for x in xrange(A):
            screen[y][x] = '#'
    return screen

def rot_row(screen, A, B):
    current_row = [screen[A][x] for x in xrange(len(screen[0]))]
    new_row = current_row[-B:] + current_row[:-B]
    for x in xrange(len(screen[0])):
        screen[A][x] = new_row[x]
    return screen

def rot_col(screen, A, B):
    current_col = [screen[y][A] for y in xrange(len(screen))]
    new_col = current_col[-B:] + current_col[:-B]
    for y in xrange(len(screen)):
        screen[y][A] = new_col[y]
    return screen

for line in data:
    if line.startswith('rect'):
        A, B = re.match(r'\w+\ (\d+)x(\d+)', line).groups()
        screen = rect(screen, int(A), int(B))

    elif line.startswith('rotate row'):
        A, B = re.match(r'\w+\ \w+\ y=(\d+)\ by\ (\d+)', line).groups()
        screen = rot_row(screen, int(A), int(B))

    elif line.startswith('rotate column'):
        A, B = re.match(r'\w+\ \w+\ x=(\d+)\ by\ (\d+)', line).groups()
        screen = rot_col(screen, int(A), int(B))

for line in screen:
    print ' '.join(line)