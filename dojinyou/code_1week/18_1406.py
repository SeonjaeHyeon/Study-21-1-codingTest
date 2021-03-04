# https://www.acmicpc.net/problem/11656

from sys import stdin
input = stdin.readline

text = input()
suffix = []
for i in range(len(text)):
	suffix.append(text[i:])
print("\n".join(sorted(suffix)))