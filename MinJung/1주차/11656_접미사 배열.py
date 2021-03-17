S = input()
Slist = []
for i in range(len(S)):
    Slist.append(S[i:])
Slist.sort()
for i in Slist:
    print(i)
