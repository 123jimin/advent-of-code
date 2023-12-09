from math import sqrt

def get_num_wins(time, dist):
    # Nah just binary search it
    x = time // 2

    if x * (time - x) <= dist:
        return 0
    
    if dist < 0: return time+1

    lb = 0
    ub = x

    while ub-lb > 1:
        x = (lb + ub) // 2
        if x * (time - x) <= dist:
            lb = x
        else:
            ub = x
    
    x = ub

    return time - 2*x + 1

with open("../input/06.txt") as f:
    times = list(int(x) for x in f.readline().split(':')[1].split() if x)
    distances = list(int(x) for x in f.readline().split(':')[1].split() if x)

ans = 1
for (time, dist) in zip(times, distances):
    ans *= get_num_wins(time, dist)

print(ans)