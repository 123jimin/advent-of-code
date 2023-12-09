graph = dict()

with open("../input/08.txt") as f:
    inst = f.readline().strip()
    f.readline()
    for l in f:
        l = l.strip()
        if not l: continue
        k, v = l.split('=')
        v = v.strip()
        graph[k.strip()] = tuple(t.strip() for t in v[1:-1].split(','))

steps = 0
curr = 'AAA'
while curr != 'ZZZ':
    curr = graph[curr][0 if inst[steps%len(inst)] == 'L' else 1]
    steps += 1

print(steps)