def find(num, arr):
    left, right = 0, len(arr)-1
    isExist = False
    while True:
        if left > right:
            break
        mid = (left + right)//2
        if num > arr[mid]:
            left = mid + 1
        elif num < arr[mid]:
            right = mid - 1
        else:
            isExist = True
            break
    return 1 if isExist else 0


N = int(input())
arr = list(map(int, input().split()))
arr.sort()
M = int(input())
arr2 = list(map(int, input().split()))
for i in arr2:
    print(find(i, arr))
