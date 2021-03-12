# https://www.acmicpc.net/problem/11652
# 카드

from sys import stdin
input = stdin.readline

n = int(input())

d = dict()
for _ in range(n):
    v = int(input())
    d[v] = d.get(v, 0) + 1

l = [k for k in d.items()]
s = sorted(l, key = lambda x: x[0])
s = sorted(s, key = lambda x: x[1], reverse=True)
print(s[0][0])
