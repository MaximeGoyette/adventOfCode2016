keypad = [
    ['0', '0', '1', '0', '0'],
    ['0', '2', '3', '4', '0'],
    ['5', '6' ,'7' ,'8' ,'9'],
    ['0', 'A', 'B', 'C', '0'],
    ['0', '0', 'D', '0', '0']
]

a = open('2.txt').read().split('\n')

code = []

def get_next_pos(pos, direction, keypad):
    if direction == 'U':
        next_pos = [max(0, pos[0] - 1), pos[1]]
    elif direction == 'D':
        next_pos = [min(4, pos[0] + 1), pos[1]]
    elif direction == 'L':
        next_pos = [pos[0], max(0, pos[1] - 1)]
    elif direction == 'R':
        next_pos = [pos[0], min(4, pos[1] + 1)]
    if keypad[next_pos[0]][next_pos[1]] != '0':
        pos = next_pos
    return pos

for instructions in a:
    pos = [2, 0]
    for x in instructions:
        pos = get_next_pos(pos, x, keypad)
    
    code.append(keypad[pos[0]][pos[1]])

print ''.join(code)