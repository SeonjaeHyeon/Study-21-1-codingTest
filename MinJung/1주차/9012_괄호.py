for i in range(int(input())):
    result = "YES"
    stack = []
    str = input()
    strL= list(str)
    for j in strL:
        if j=="(":
            stack.append("(")
        elif j==")":
            if stack == []:
                result="NO"
                break
            stack.pop()
    if stack!=[]:
        result = "NO"
    print(result)

            

