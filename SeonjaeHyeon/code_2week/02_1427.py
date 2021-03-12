# https://www.acmicpc.net/problem/1427
# 소트인사이드

from sys import stdin
input = stdin.readline

def bubble_desc(s):
    l = len(s)
    for i in range(l - 1):
        swaped = False
        for j in range(l - i - 1):
            if s[j] < s[j + 1]:
                swaped = True
                s[j], s[j + 1] = s[j + 1], s[j]

        if not swaped:
            return s

    return s

nums = list(input().rstrip())
print(''.join(bubble_desc(nums)))
