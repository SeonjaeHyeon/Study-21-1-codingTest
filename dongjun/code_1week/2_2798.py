def check(arr, cache, M):
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            for k in range(j, len(arr)):
                if(i == j or j == k or k == i):
                    continue
                temp = arr[i]+arr[j]+arr[k]
                if temp <= M:
                    cache.append(temp)
    return max(cache)


N, M = map(int, input().split())
arr = list(map(int, input().split()))
cache = []
print(check(arr, cache, M))
