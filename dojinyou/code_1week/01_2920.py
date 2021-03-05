# https://www.acmicpc.net/problem/2920

from sys import stdin
input = stdin.readline

# solution 1
input_list = list(map(int, input().split()))

is_ascending = True
is_descending = True
for i in range(1,8):
	if input_list[i-1] < input_list[i]:
		is_descending = False
	elif input_list[i-1] > input_list[i]:
		is_ascending = False

if is_ascending :
	print("ascending")
elif is_descending :
	print("descending")
else :
	print("mixed")

# # solution 2
# input_list = list(map(int, input().split()))
# if input_list[0] != '1' and input_list[0] != '8' :
#   result = "mixed"
# else :
# 	salt = 1 if input_list[0]=='1' else -1
# 	result = "ascending" if input_list[0]=='1' else "descending"
# 	for i in range(len(input_list)-1) :
# 		if int(input_list[i]) + salt != int(input_list[i+1]):
# 			result = "mixed"
# 			break

# print(result)