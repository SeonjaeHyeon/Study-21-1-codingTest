from collections import defaultdict
import sys
import operator

d = defaultdict(int)
N=int(sys.stdin.readline())
for i in range(N):
    d[int(sys.stdin.readline())]+=1
d= dict(d)
l=[key for m in [max(d.values())] for key,val in d.items() if val == m]
l.sort()
print(l[0])
