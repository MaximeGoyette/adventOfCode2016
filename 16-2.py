data = '01111010110010011'
size = 35651584

while len(data) < size:
    a = data
    b = a
    b = b[::-1]
    b = b.replace('0', 'a').replace('1', '0').replace('a', '1')
    data = a + '0' + b

data = data[:size]
chcksm = data

while len(chcksm)%2==0:
    chcksm = ''.join(['1' if len(set(chcksm[i:i+2])) == 1 else '0' for i in range(0, len(chcksm), 2)])

print(chcksm)
