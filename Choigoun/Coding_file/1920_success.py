#Binary Search 이용하기
def BinarySearch(arr, val, low, high):
    if low > high:
        return False
    
    mid = (low + high) // 2
    if arr[mid] > val:
        return BinarySearch(arr, val, low, mid - 1)
    elif arr[mid] < val:
        return BinarySearch(arr, val, mid + 1, high)
    else:
        return True



num1 = int(input()) # 숫자
numlist = list(map(int,input().split())) # 리스트
M = int(input()) # 몇 줄
M_list = list(map(int,input().split()))
numlist = sorted(numlist) # 오름차순 정렬하기

for m in M_list :
    if BinarySearch(numlist,m,0,num1-1):
        print(1)
    else:
        print(0)