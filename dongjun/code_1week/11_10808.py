string = list(str(input()))
alphabet = 'abcdefghijklmnopqrstuvwxyz'
res = [0]*len(alphabet)
for s in string:
    idx = alphabet.index(s)
    res[idx] += 1
for r in res:
    print(r, end=" ")
