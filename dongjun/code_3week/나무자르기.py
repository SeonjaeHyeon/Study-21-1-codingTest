import sys
N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
arr.reverse()

left, right = 1, arr[0]
while True:
    if left > right:
        break
    mid = (left + right) // 2
    temp = 0
    for i in arr:
        if i >= mid:
            temp += i-mid
        else:
            break
    if temp >= M:
        left = mid + 1
    else:
        right = mid - 1
sys.stdout.write(str(right))
