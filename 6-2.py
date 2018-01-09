from collections import Counter

a = open('6.txt').read().split('\n')

message = ''

for i in range(len(a[0])):
    c = Counter([x[i] for x in a])
    message += c.most_common()[:-1-1:-1][0][0]

print message