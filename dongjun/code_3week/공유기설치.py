N, C = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(int(input()))
arr.sort()
# print(arr)
left, right = 0, arr[-1]-arr[0]
res = 0
while True:
    if left > right:
        break
    mid = (left + right) // 2
    cnt = 1
    idx = 0
    for i in range(1, len(arr)):
        if arr[i] >= arr[idx] + mid:
            cnt += 1
            idx = i
    if cnt >= C:
        left = mid + 1
        res = mid
    else:
        right = mid - 1
print(res)
