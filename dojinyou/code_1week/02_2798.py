# https://www.acmicpc.net/problem/2798

from sys import stdin
input = stdin.readline

# solution 1
from itertools import combinations
n, m =map(int, input().split())
numbers = list(map(int, input().split()))
print(max(map(lambda x:sum(x) if sum(x)<=m else -1, combinations(numbers,3))))

# solution 2
n, m =map(int, input().split())
numbers = list(map(int, input().split()))
result = 0
for i in range(n-2):
	for j in range(i+1,n-1):
		for k in range(j+1,n):
			if result < numbers[i]+numbers[j]+numbers[k] <= m :
				result = numbers[i]+numbers[j]+numbers[k]
print(result)
