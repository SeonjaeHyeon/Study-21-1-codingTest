def check(target):
    cnt = 0
    for i in target:
        if cnt < 0:
            return "NO"
        if i == "(":
            cnt += 1
        elif i == ")":
            cnt -= 1
    if cnt == 0:
        return "YES"
    else:
        return "NO"


N = int(input())
arr = []
for _ in range(N):
    arr.append(input())

for e in arr:
    print(check(e))
