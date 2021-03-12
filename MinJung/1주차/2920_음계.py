"""다장조는 c d e f g a b C, 총 8개 음으로 이루어져있다. 이 문제에서 8개 음은 다음과 같이 숫자로 바꾸어 표현한다. c는 1로, d는 2로, ..., C를 8로 바꾼다.

1부터 8까지 차례대로 연주한다면 ascending, 8부터 1까지 차례대로 연주한다면 descending, 둘 다 아니라면 mixed 이다.

연주한 순서가 주어졌을 때, 이것이 ascending인지, descending인지, 아니면 mixed인지 판별하는 프로그램을 작성하시오.
"""
L =  [int(x) for x in input().split()]
num = 1
if L[0]==1:
    for i in range(len(L)-1):
        num+=1
        if L[i]+1 != L[i+1]:
            print("mixed")
            break
    if num==8:
        print("ascending")
elif L[0]==8:
    for i in range(len(L)-1):
        num+=1
        if L[i]-1 != L[i+1]:
            print("mixed")
            break
    if num==8:
        print("descending")
else:
    print("mixed")
