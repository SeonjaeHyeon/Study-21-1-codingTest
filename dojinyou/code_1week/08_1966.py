# https://www.acmicpc.net/problem/1966

from collections import deque
from sys import stdin
input = stdin.readline

for _ in range(int(input().rstrip())):
	n, target = map(int, input().split())
	q = deque(list(enumerate(input().split())))
	cnt = 1
	while q :
		max_w = max(q, key=lambda x:x[1])[1]
		item = q.popleft()
		if item[1] == max_w :
			if item[0] == target :
				print(cnt)
				break
			cnt += 1
		else :
			q.append(item)