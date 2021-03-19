N = int(input())
arr = list(map(int, input().split()))
cache = dict()
for i in arr:
    if cache.get(i):
        cache[i] += 1
    else:
        cache[i] = 1
M = int(input())
arr2 = list(map(int, input().split()))
for i in arr2:
    print(cache.get(i) if cache.get(i) else 0)
