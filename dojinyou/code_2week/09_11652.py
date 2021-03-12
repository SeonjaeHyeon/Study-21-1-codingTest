# https://www.acmicpc.net/problem/11652

from sys import stdin
input = stdin.readline

students = {}
for _ in range(int(input())):
	name, kor, eng, math = input().rstrip().split()
	students[name] = [int(kor), int(eng), int(math)]
[print(name) for name, _ in sorted(students.items(),key=lambda x:(-x[1][0],x[1][1],-x[1][2],x[0]))]