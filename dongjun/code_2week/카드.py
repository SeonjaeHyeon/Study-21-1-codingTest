N = int(input())
cache = {}
for _ in range(N):
    temp = int(input())
    if temp in cache:
        cache[temp] += 1
    else:
        cache[temp] = 1
res = sorted(cache.items(), key=lambda a: (-a[1], a[0]))
print(res[0][0])
