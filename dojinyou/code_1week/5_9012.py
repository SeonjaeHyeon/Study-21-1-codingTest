# https://www.acmicpc.net/problem/9012

from sys import stdin
input = stdin.readline
n = int(input().rstrip())
for _ in range(n):
	PS = input().rstrip()
	stack = []
	is_VPS = True
	
	for c in PS :
		if c == "(":
			stack.append(c)
		elif c == ")":
			if len(stack) == 0 :
				is_VPS = False
				break
			stack.pop()

	if len(stack) != 0:
		is_VPS = False

	print("YES" if is_VPS else "NO")


