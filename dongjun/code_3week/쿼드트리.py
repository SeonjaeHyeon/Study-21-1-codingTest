def solve(arr):
    global res
    temp = arr[0][0]
    for i in arr:
        for j in i:
            if j != temp:
                length = len(arr)//2
                for a in range(2):
                    for b in range(2):
                        cache = arr[(a*length):((a+1)*length)]
                        for k in range(len(cache)):
                            cache[k] = cache[k][(b*length):((b+1)*length)]
                        idx = len(res)
                        if not solve(cache):
                            res.insert(idx, "(")
                            res.append(")")
                return False
    res.append(temp)
    return True


N = int(input())
arr = []
for _ in range(N):
    arr.append(list(input()))
res = ["("]
solve(arr)
res.append(")")
for i in res:
    print(i, end="")
