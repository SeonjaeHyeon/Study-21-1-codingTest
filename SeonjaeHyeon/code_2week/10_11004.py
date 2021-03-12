# https://www.acmicpc.net/problem/11004
# K번째 수

from sys import stdin
input = stdin.readline

n, v = map(int, input().split())

s = sorted(map(int, input().split()))
print(s[v - 1])
