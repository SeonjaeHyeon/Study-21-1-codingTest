n1 = int(input())
a1 = input().split(' ')
n2 = int(input())
a2 = input().split(' ')

a1.sort()

for e in a2:
    low = 0
    high = n1 - 1
    flag = False

    while low <= high:
        mid = (low + high) // 2

        if e == a1[mid]:
            flag = True
            break
        
        if e < a1[mid]:
            high = mid - 1
        else:
            low = mid + 1

    if flag:
        print(1)
    else:
        print(0)
