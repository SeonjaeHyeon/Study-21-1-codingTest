x = [-1 for _ in range(26)]

for i, c in enumerate(input()):
    v = ord(c) - 97

    if x[v] != -1:
        continue

    x[v] = i

print(' '.join(map(str, x)))
