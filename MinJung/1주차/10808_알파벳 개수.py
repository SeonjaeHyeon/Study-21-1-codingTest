str = list(input())
strL = [0] * 26
type(str)
for i in str:
    strL[ord(i)-97]+=1
for i in strL:
    print(i, end = ' ')