from collections import defaultdict

reg = defaultdict(int)
reg['c'] = 1

data = open('12.txt').read().split('\n')

i = 0

while i < len(data):
    line = data[i]

    if line.startswith('cpy'):
        args = line.split()[1:]
        x = reg[args[0]] if not args[0].isdigit() else int(args[0])
        y = args[1]
        reg[y] = x
    elif line.startswith('inc'):
        x = line.split(' ')[-1]
        reg[x] += 1
    elif line.startswith('dec'):
        x = line.split(' ')[-1]
        reg[x] -= 1
    elif line.startswith('jnz'):
        args = line.split()[1:]
        x = reg[args[0]] if not args[0].isdigit() else int(args[0])
        y = int(args[1])
        if x != 0:
            i += y - 1

    i += 1

print(reg['a'])
