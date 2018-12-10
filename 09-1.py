data = open('9.txt').read()

decompressed = []

i = 0

while i < len(data):
    if data[i] == '(':
        j = data.find(')', i)
        marker = data[i + 1:j]
        n = int(marker.split('x')[0])
        r = int(marker.split('x')[1])
        i = j+1

        data_to_repeat = []
        for _ in xrange(n):
            data_to_repeat.append(data[i])
            i += 1
        decompressed.extend(data_to_repeat*r)

    else:
        decompressed.append(data[i])
        i += 1

print len(decompressed)