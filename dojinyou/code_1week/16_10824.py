# https://www.acmicpc.net/problem/10824

from sys import stdin
input = stdin.readline

num = input().split()
print(int(num[0]+num[1])+int(num[2]+num[3]))