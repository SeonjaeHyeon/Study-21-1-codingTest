def solve(arr):
    global res
    temp = arr[0][0]
    for i in arr:
        for j in i:
            if j != temp:
                length = len(arr)//3
                for a in range(3):
                    for b in range(3):
                        cache = arr[(a*length):((a+1)*length)]
                        for k in range(len(cache)):
                            cache[k] = cache[k][(b*length):((b+1)*length)]
                        solve(cache)
                return
    res[temp+1] += 1
    return


N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))
res = [0, 0, 0]
solve(arr)
for i in res:
    print(i, end=" ")
