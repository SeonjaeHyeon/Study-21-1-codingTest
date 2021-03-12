# https://www.acmicpc.net/problem/1427

from sys import stdin
input = stdin.readline

print("".join(sorted([c for c in input().rstrip()], reverse=True)))
