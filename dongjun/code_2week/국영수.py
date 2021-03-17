N = int(input())
arr = []
for _ in range(N):
    arr.append(input().split())

arr.sort(key=lambda a: (-int(a[1]), int(a[2]), -int(a[3]), a[0]))

for x in arr:
    print(x[0])
