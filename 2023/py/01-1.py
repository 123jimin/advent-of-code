def extract(line):
    first = last = None
    for c in line:
        if c.isnumeric():
            if first is None: first = c
            last = c
    
    if first is None:
        return 0
    else:
        return int(first+last)

with open("../input/01.txt") as f:
    print(sum(map(extract, f)))