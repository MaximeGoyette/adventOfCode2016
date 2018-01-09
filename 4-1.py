a = open('4.txt').read()

b = []

d = 'abcdefghijklmnopqrstuvwxyz'

def rot(s, n):
    return ''.join([d[(d.index(x) + n)%len(d)] for x in s])

for x in a.split('\n'):
    checksum = x[-6:-1]
    x = x[:-7].split('-')
    sector_id = int(x[-1])
    y = x[:-1]
    x = ''.join(x[:-1])
    x = ''.join(sorted(sorted(list(set(x))), key=lambda y: x.count(y), reverse=True)[:5])
    if x == checksum:
        if 'northpole' in ' '.join([rot(z, sector_id) for z in y]):
            print sector_id