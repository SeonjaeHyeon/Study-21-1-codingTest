# https://www.acmicpc.net/problem/2751
# 수 정렬하기 2

from sys import stdin
input = stdin.readline

n = int(input())

nums = sorted([int(input()) for _ in range(n)])
for i in nums:
    print(i)
