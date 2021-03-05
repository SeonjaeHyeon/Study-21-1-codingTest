import sys

while True:
    x = [0 for _ in range(4)]

    s = sys.stdin.readline().strip('\n')
    if s == '':
        break

    for c in s:
        if 'a' <= c <= 'z':
            x[0] += 1
        elif 'A' <= c <= 'Z':
            x[1] += 1
        elif c.isdigit():
            x[2] += 1
        else:
            x[3] += 1

    print(' '.join(map(str, x)))
