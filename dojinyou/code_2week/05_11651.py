# https://www.acmicpc.net/problem/11651

from sys import stdin
input = stdin.readline

locations = {}
for _ in range(int(input())):
	x, y = map(int, input().split())
	if locations.get(y):
		locations[y].append(x)
	else :
		locations[y] = [x]
[print(x, y) for y, x_list in sorted(locations.items()) for x in sorted(x_list)]