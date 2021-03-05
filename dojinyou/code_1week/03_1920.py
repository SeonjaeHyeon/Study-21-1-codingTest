# https://www.acmicpc.net/problem/1920

from sys import stdin
input = stdin.readline

# solution 1
def in_number(sorted_array, number):
	left_index = 0
	right_index = len(sorted_array)-1
	while left_index <= right_index :
		m = (left_index+right_index)//2
		if sorted_array[m] == number :
			return True
		if sorted_array[m] < number :
			left_index = m+1
		elif sorted_array[m] > number :
			right_index = m-1
	return False
n = int(input().rstrip())
array = list(map(int, input().split()))
array.sort()
m = int(input().rstrip())
numbers = list(map(int, input().split()))
for number in numbers :
	print(int(in_number(array, number)))


# solution 2
n = int(input().rstrip())
dic = {item:1 for item in input().split()}
m = int(input().rstrip())
numbers = input().split()
for number in numbers :
	print("1" if dic.get(number) else "0")
