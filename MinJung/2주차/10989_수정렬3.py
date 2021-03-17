import sys
l=[]
N=int(sys.stdin.readline())
for i in range(N):
    l.append(int(sys.stdin.readline()))
l.sort()
for i in l:
    print(i)