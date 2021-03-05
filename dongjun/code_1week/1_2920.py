def check(arr, start):
    cnt = 0
    if start == 1:
        cnt = 1
    elif start == 8:
        cnt = -1
    else:
        return "mixed"

    predict = start
    for i in arr:
        if predict != i:
            return "mixed"
        predict += cnt
    return "ascending" if start == 1 else "descending"


arr = list(map(int, input().split()))
print(check(arr, arr[0]))
