arg = input().split(' ')
x = list(map(int, input().split(' ')))

n = int(arg[1])
x.sort()

# 사용할 수 없는 수 제거
a, b = x[0:2]
for i in x[2:]:
    if a + b + i > n:
        x.remove(i)

l = len(x)
y = []
for i in range(l - 2):
    for j in range(i + 1, l - 1):
        for k in range(j + 1, l):
            v = x[i] + x[j] + x[k]
            if v <= n:
                y.append(v)

print(max(y))
