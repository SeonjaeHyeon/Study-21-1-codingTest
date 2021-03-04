# https://www.acmicpc.net/problem/10808

from sys import stdin
input = stdin.readline

text = input().strip()
countList = [0]*26

for c in text:
	countList[ord(c)-97] += 1

print(" ".join(map(str,countList)))
