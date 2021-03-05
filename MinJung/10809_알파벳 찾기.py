str = list(input())
strL = [-1] * 26

for i in range(len(str)):
    if strL[ord(str[i])-97]==-1:
        strL[ord(str[i])-97]=i
for i in strL:
    print(i, end = ' ')