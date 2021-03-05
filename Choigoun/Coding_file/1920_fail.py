
a = int(input())
b = input()
c = int(input())
d = input()


b = b.split(' ')
d = d.split(' ')

# 모든 리스트 요소를 숫자로 만들기
for i in range(a):
    b[i] = int(b[i])

for i in range(c):
    d[i] = int(d[i])


for i in d:
    num = 0
    for j in b:
        if i == j:
            num+=1
    if num != 0:
        print("1")
    else:
        print("0")
    