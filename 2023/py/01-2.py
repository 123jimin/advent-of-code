NUMBERS = dict((['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'][i], i) for i in range(10))
NUMBERS_REV = dict((w[::-1], i) for (w, i) in NUMBERS.items())

def get_first_number(line, spells):
    for i in range(len(line)):
        c = line[i]
        if c.isnumeric():
            return int(c)
        for (w, n) in spells.items():
            if w[0] == c and line[i:i+len(w)] == w:
                return n
    return None

def extract_value(line):
    first = get_first_number(line, NUMBERS)
    last = get_first_number(line[::-1], NUMBERS_REV)
    if first is None or last is None: return 0
    return first*10 + last

with open("../input/01.txt") as f:
    print(sum(map(extract_value, f)))