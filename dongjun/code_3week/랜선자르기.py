K, N = map(int, input().split())
arr = []
for _ in range(K):
    arr.append(int(input()))

left, right = 1, max(arr)
while True:
    if left > right:
        break
    mid = (left + right) // 2
    cnt = 0
    for i in arr:
        cnt += i//mid
    if cnt >= N:
        left = mid + 1
    else:
        right = mid - 1
print(right)
