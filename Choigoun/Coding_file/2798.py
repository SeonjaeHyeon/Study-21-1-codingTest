
input_1 = input()
input_2 = input()
num = int(input_1.split(' ')[0])
max_num = int(input_1.split(' ')[1])

num_list = input_2.split(' ')

# 모든 리스트 요소를 숫자로 만들기
for i in range(num):
    num_list[i] = int(num_list[i])

guess_num = 0
for i in range(num-2):
    for a in range(i+1,num-1):
        for b in range(a+1,num):
            sum_num = num_list[i] + num_list[a] + num_list[b]
            if sum_num <= max_num and sum_num > guess_num:
                guess_num = sum_num

print(guess_num)