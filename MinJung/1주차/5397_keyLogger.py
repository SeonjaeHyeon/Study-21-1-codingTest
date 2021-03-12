"""stack 두개 만들어서 넣었다 뺏다 해보자"""
num = int(input(""))
for i in range(num):
    index = 0
    keyS = input("")
    key = list(keyS)
    final_str = []
    for i in key:
        if i =="<" and index !=0:
            index -=1
        elif i ==">" and index != len(final_str):
            index +=1
        elif i == "-" and final_str != []:
            if index != 0:
                index-=1
                final_str.pop(index)
        elif i!="<" and i !=">" and i != "-":
            final_str.insert(index,i)
            index+=1
    print(''.join(final_str))

