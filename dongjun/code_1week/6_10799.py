parentheses = input()
pair = [0]*len(parentheses)
cnt = 0
idx = 0
for i in range(len(parentheses)):
    if i != 0 and parentheses[i] == ")" and parentheses[i-1] == "(":
        pair[i-1], pair[i] = -1, -1
        idx -= 1
        continue
    if parentheses[i] == "(":
        idx += 1
        pair[i] = idx
    elif parentheses[i] == ")":
        pair[i] = idx
        idx -= 1
print(pair)
cnt = max(pair)
res = 0
temp = 0
for i in range(1, cnt+1):
    for j in range(pair.index(i), len(pair)):
        print(j)
        if j != pair.index(i) and pair[j] == i:
            break
        if pair[j] == -1:
            temp += 1
    res += temp/2
print(res)
