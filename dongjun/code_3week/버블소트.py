def bubble_sort(arr):
    cnt = 0
    length = len(arr) - 1
    for i in range(length):
        for j in range(length-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                cnt += 1
    return cnt


N = int(input())
arr = list(map(int, input().split()))
print(bubble_sort(arr))
