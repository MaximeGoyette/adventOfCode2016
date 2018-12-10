data = open('9.txt').read()

def process(data):
    total = 0
    while data:
        i = data.find('(')
        if i > 0:
            total += i
            data = data[i:]
        try:
            marker, data = tuple(data.split(')', 1))
        except:
            return len(data)

        n, m = tuple(map(int, marker[1:].split('x')))

        try:
            total += process(data[:n])*m
        except:
            pass

        data = data[n:]

    return total

print process(data)