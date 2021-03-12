# https://www.acmicpc.net/problem/10825
# 국영수

from sys import stdin
input = stdin.readline

n = int(input())

s = []
for _ in range(n):
    v = input().split()
    t = [v[0]]
    t.extend(map(int, v[1:]))
    s.append(t)

s = sorted(s, key = lambda x: x[0])
s = sorted(s, key = lambda x: x[3], reverse=True)
s = sorted(s, key = lambda x: x[2])
s = sorted(s, key = lambda x: x[1], reverse=True)

for e in s:
    print(e[0])
