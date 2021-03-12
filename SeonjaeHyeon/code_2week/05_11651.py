# https://www.acmicpc.net/problem/11651
# 좌표 정렬하기 2

from sys import stdin
input = stdin.readline

n = int(input())

s = sorted([list(map(int, input().split())) for _ in range(n)], key = lambda x: (x[1], x[0]))

for e in s:
    print('%s %s' % (e[0], e[1]))
