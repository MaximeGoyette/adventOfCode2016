keypad = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7' ,'8' ,'9']
]

a = open('2.txt').read().split('\n')

code = []

def get_next_pos(pos, direction):
    if direction == 'U':
        pos[0] = max(0, pos[0] - 1)
    elif direction == 'D':
        pos[0] = min(2, pos[0] + 1)
    elif direction == 'L':
        pos[1] = max(0, pos[1] - 1)
    elif direction == 'R':
        pos[1] = min(2, pos[1] + 1)
    return pos

for instructions in a:
    pos = [1, 1]
    for x in instructions:
        pos = get_next_pos(pos, x)
    
    code.append(keypad[pos[0]][pos[1]])

print ''.join(code)