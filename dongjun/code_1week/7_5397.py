def left(target):
    if target == 0:
        return target
    target -= 1
    return target


def right(target, maxIdx):
    if target == maxIdx:
        target = maxIdx
        return target
    target += 1
    return target


def check(arr):
    res = []
    maxIdx = len(res)-1
    target = 0
    for i in range(len(arr)):
        if i == 0:
            res.append(arr[i])
            target = left(target)
        if arr[i] == "<":
            target = left(target)
        elif arr[i] == ">":
            target = right(target, maxIdx)
        elif arr[i] == "-":
            del res[target]
            target = left(target)
        else:
            res.insert(target, arr[i])

    return "".join(res)


N = int(input())
for _ in range(N):
    print(check(list(input())))
