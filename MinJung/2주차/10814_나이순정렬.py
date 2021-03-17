from collections import defaultdict
import sys

d = defaultdict(list)
N = int(sys.stdin.readline())
for i in range(N):
    l=sys.stdin.readline().split()
    d[int(l[0])].append(l[1])
newd = list(d.keys())
newd.sort()
for i in newd:
    for j in d[i]:
        print(i, j)