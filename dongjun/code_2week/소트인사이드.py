N = list(input())
N.sort(key=lambda a: -int(a))
for x in N:
    print(x, end="")
