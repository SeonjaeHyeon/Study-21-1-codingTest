N = int(input())
arr = []
for i in range(N):
    arr.append(input().split())
    arr[i].append(i)
arr.sort(key=lambda a: (int(a[0]), a[-1]))
for x in arr:
    print(x[0], x[1])
