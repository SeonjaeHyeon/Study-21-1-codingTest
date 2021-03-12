# https://www.acmicpc.net/problem/2751

from sys import stdin
input = stdin.readline

n = int(input())
countList = [0]*10001
for _ in range(n) :
    countList[int(input())] += 1
for i,c in enumerate(countList):
    [print(i) for _ in range(c)]