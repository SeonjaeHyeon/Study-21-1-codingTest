
num_string = input()
num_list = num_string.split(' ')
# num_list = ['1', '2', '3', '4', '5', '6', '7', '8']

a = 0

for i in range(7):
    if int(num_list[i])+1 == int(num_list[i+1]):
        a+=1
    if int(num_list[i]) == int(num_list[i+1])+1:
        a-=1

if a==7:
    print("ascending")
elif a==-7:
    print("descending")
else:
    print("mixed")    