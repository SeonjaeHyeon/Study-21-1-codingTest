L = list(input())
stack = []
num=0
for i in range(len(L)):
    if L[i]=="(":
        stack.append("(")
    elif L[i]==")":
        if L[i-1]=="(":
            stack.pop()
            num+=len(stack)
        else:
            stack.pop()
            num+=1
            

print(num)


