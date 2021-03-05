import sys

k = []

def recursion(v):
    if not v:
        return 'NO' if k else 'YES'

    if v[0] == '(':
        k.append(0)
    else:
        try:
            k.pop()
        except IndexError:
            return 'NO'
    
    return recursion(v[1:])

n = int(input())

for _ in range(n):
    s = sys.stdin.readline().rstrip()

    k.clear()
    print(recursion(s))
