import md5

a = open('5.txt').read()

i = 0

passw = [None]*8

while None in passw:
    h = md5.new(a + str(i)).hexdigest()
    if h.startswith('0'*5) and h[5].isdigit() and int(h[5]) in range(8) and passw[int(h[5])] == None:
        passw[int(h[5])] = h[6]
        print passw
    i += 1

print ''.join(passw)