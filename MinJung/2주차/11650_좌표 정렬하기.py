from collections import defaultdict

d = defaultdict(list)
N = int(input())
for i in range(N):
    l=input().split()
    print(l)
    d[int(l[0])].append(int(l[1]))
    d[int(l[0])].sort()
newd = list(d.keys())
newd.sort()
for i in newd:
    for j in d[i]:
        print(i,j)





