# https://www.acmicpc.net/problem/10825
# 수 정렬하기 3

from sys import stdin
input = stdin.readline

n = int(input())
s = dict()

for _ in range(n):
    v = int(input())
    s[v] = s.get(v, 0) + 1

for c in sorted(s.keys()):
    print((('%s\n' % c) * s[c]).rstrip())
