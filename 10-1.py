import re
import pydash

data = '''value 5 goes to bot 2
bot 2 gives low to bot 1 and high to bot 0
value 3 goes to bot 1
bot 1 gives low to output 1 and high to bot 0
bot 0 gives low to output 2 and high to output 0
value 2 goes to bot 2'''.split('\n')

data = open('10.txt').read().split('\n')

data.sort()

bots = {}
outputs = {}

couple_to_find = set([61, 17])

for x in data:
    if x.startswith('value'):

        m = re.match(r'value (\d+) goes to (.*)', x)
        value, bot = m.groups()

        if not 'values' in bots[bot]:
            bots[bot]['values'] = set()
        bots[bot]['values'].add(int(value))

    else:
        m = re.match(r'(.*) gives low to (.*) and high to (.*)', x)
        bot, lowbot, highbot = m.groups()
        if not bot in bots:
            bots[bot] = {}
        if 'output' in lowbot and not lowbot in outputs:
            outputs[lowbot] = set()
        elif not lowbot in bots:
            bots[lowbot] = {}
        if 'output' in highbot and not highbot in outputs:
            outputs[highbot] = set()
        elif not highbot in bots:
            bots[highbot] = {}

        bots[bot]['low'] = lowbot
        bots[bot]['high'] = highbot

while any([len(bots[b].get('values', set())) >= 2 for b in bots]):
    cbot = [b for b in bots if len(bots[b].get('values', set())) >= 2][0]

    if bots[cbot]['values'] == couple_to_find:
        print cbot
        exit()

    min_val = min(bots[cbot]['values'])
    bots[cbot]['values'].remove(min_val)
    max_val = max(bots[cbot]['values'])
    bots[cbot]['values'].remove(max_val)

    lowbot = bots[cbot]['low']
    highbot = bots[cbot]['high']

    if 'output' in lowbot:
        outputs[lowbot].add(min_val)
    else:
        if not 'values' in bots[lowbot]:
            bots[lowbot]['values'] = set()
        bots[lowbot]['values'].add(min_val)

    if 'output' in highbot:
        outputs[highbot].add(max_val)
    else:
        if not 'values' in bots[highbot]:
            bots[highbot]['values'] = set()
        bots[highbot]['values'].add(max_val)
