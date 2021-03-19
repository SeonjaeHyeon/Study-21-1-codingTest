N = int(input())
cache = [0]*(N+1)
for i in range(N+1):
    if i == 0:
        continue
    if i == 1:
        cache[i] = 1
        continue
    cache[i] = cache[i-1] + cache[i-2]
print(cache[N])
