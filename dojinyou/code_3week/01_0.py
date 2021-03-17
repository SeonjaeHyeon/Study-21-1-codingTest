# https://www.acmicpc.net/problem/2750

from sys import stdin
input = stdin.readline

[print(num) for num in sorted([int(input()) for _ in range(int(input()))])]