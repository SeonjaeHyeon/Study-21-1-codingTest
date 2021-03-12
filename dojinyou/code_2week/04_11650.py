# https://www.acmicpc.net/problem/11650

from sys import stdin
input = stdin.readline

locations = {}
for _ in range(int(input())):
	x, y = map(int, input().split())
	if locations.get(x):
		locations[x].append(y)
	else :
		locations[x] = [y]
[print(x, y) for x, y_list in sorted(locations.items()) for y in sorted(y_list)]