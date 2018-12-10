import md5

a = open('5.txt').read()

i = 0

passw = ''

while True:
    h = md5.new(a + str(i)).hexdigest()
    if h.startswith('0'*5):
        passw += h[5]
        print passw
    i += 1
    if len(passw) >= 8:
        break