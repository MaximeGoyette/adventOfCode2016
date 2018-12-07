import re

a = open('7.txt').read().split('\n')

def supports_tls(ip):
    interiors = []
    exteriors = []

    for x in re.findall(r'\[(\w+)\]', ip):
        for i in xrange(len(x) - 3):
            interiors.append(x[i:i+4])

    for x in re.split(r'\[\w+\]', ip):
        for i in xrange(len(x) - 3):
            exteriors.append(x[i:i+4])

    for x in interiors:
        if x[0] == x[3] and x[1] == x[2] and x[0] != x[1]:
            return False

    for x in exteriors:
        if x[0] == x[3] and x[1] == x[2] and x[0] != x[1]:
            return True

    return False

print len([ip for ip in a if supports_tls(ip)])