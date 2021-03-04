# https://www.acmicpc.net/problem/1168

from sys import stdin

n, k = map(int,input().split())
array = [i+1 for i in range(n)]
removeIndex = k-1
mod = n
result = []
for _ in range(n):
	result.append(str(array.pop(removeIndex)))
	if mod != 1 :
		mod -= 1
		removeIndex = (removeIndex-1+k)%mod
print(f'<{", ".join(result)}>')