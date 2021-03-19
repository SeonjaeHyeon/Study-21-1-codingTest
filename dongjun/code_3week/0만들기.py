def solve(num, arr):
    global res
    arr.append(str(num))
    if num == N:
        temp = arr.copy()
        while " " in temp:
            temp.remove(" ")
        temp = "".join(temp)
        if eval(temp) == 0:
            temp = "".join(arr)
            res.append(temp)
        return
    cache = arr.copy()
    cache.append("+")
    solve(num+1, cache)
    cache = arr.copy()
    cache.append("-")
    solve(num+1, cache)
    cache = arr.copy()
    cache.append(" ")
    solve(num+1, cache)


res = []
for _ in range(int(input())):
    N = int(input())
    solve(1, [])
    res.sort()
    for i in res:
        print(i)
    res = []
    print()
