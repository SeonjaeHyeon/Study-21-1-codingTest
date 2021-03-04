# https://www.acmicpc.net/problem/10809

from sys import stdin
input = stdin.readline

text = input().rstrip()
countList = [-1]*26

for i, c in enumerate(text):
	alphaIndex = ord(c)-97
	if countList[alphaIndex] == -1 :
		countList[alphaIndex] = i  

print(" ".join(map(str,countList)))
