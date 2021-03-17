arr = []
N = int(input())
for _ in range(N):
    arr.append(int(input()))
arr.sort()
for i in range(N):
    print(arr[i])
