# https://www.acmicpc.net/problem/11004

from sys import stdin
input = stdin.readline

N, K = map(int,input().split())
num_list = list(map(int, input().split()))
print(sorted(num_list)[K-1])