import re

a = open('7.txt').read().split('\n')

def supports_ssl(ip):
    interiors = []
    exteriors = []

    for x in re.findall(r'\[(\w+)\]', ip):
        for i in xrange(len(x) - 2):
            interiors.append(x[i:i+3])

    for x in re.split(r'\[\w+\]', ip):
        for i in xrange(len(x) - 2):
            exteriors.append(x[i:i+3])

    for x in interiors:
        if x[0] == x[2] and x[1]+x[0]+x[1] in exteriors:
            return True
    return False


print len([ip for ip in a if supports_ssl(ip)])