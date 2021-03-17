# https://www.acmicpc.net/problem/10814

from sys import stdin
input = stdin.readline

members = {}
for _ in range(int(input())):
	age, name = input().rstrip().split()
	if members.get(int(age)):
		members[int(age)].append(name)
	else :
		members[int(age)] = [name]
[print(age, name) for age, name_list in sorted(members.items()) for name in name_list]