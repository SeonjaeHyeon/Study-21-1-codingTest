# https://www.acmicpc.net/problem/10814
# 나이순 정렬

from sys import stdin
input = stdin.readline

n = int(input())

# https://stackoverflow.com/q/10308939
s = [(int(x[0]), x[1]) for x in (input().split() for _ in range(n))]

for e in sorted(s, key = lambda x: x[0]):
    print('%s %s' % (e[0], e[1]))
