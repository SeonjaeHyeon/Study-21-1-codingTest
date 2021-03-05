s = input()
n = len(s)
x = []

for i in range(n):
    x.append(s[i:n])

print('\n'.join(sorted(x)))
