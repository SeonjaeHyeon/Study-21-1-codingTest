import sys
N = int(sys.stdin.readline())
cache = [0] * 10001
for i in range(N):
    cache[int(sys.stdin.readline())] += 1
for i in range(10001):
    if cache[i] != 0:
        for j in range(cache[i]):
            sys.stdout.write(str(i)+"\n")
