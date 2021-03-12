# https://www.acmicpc.net/problem/2750
# 수 정렬하기

from sys import stdin
input = stdin.readline

def bubble(s):
    l = len(s)
    for i in range(l - 1):
        swaped = False
        for j in range(l - i - 1):
            if s[j] > s[j + 1]:
                swaped = True
                s[j], s[j + 1] = s[j + 1], s[j]

        if not swaped:
            return s

    return s

n = int(input())

nums = bubble([int(input()) for _ in range(n)])
for i in nums:
    print(i)
