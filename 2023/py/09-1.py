def extrapolate(A):
    if all(A[0] == a for a in A):
        return A[0]
    diffs = [A[i] - A[i-1] for i in range(1, len(A))]
    return A[-1] + extrapolate(diffs)

with open("../input/09.txt") as f:
    print(sum(extrapolate(list(map(int, line.strip().split(' ')))) for line in f if line.strip()))