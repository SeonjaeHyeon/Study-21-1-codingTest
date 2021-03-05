import sys 

stack = [] 
def push(X):
    stack.append(X)
def pop():
    if stack == []:
        return -1
    return stack.pop()
def size():
    return len(stack)
def empty():
    if stack==[]:
        return 1
    else:
        return 0
def top():
    if stack ==[]:
        return(-1)
    return int(stack[len(stack)-1])

funcMap ={
    "push":push,
    "pop":pop,
    "size":size,
    "empty":empty,
    "top":top
}

num = int(sys.stdin.readline())
for i in range(num):
    order = sys.stdin.readline().rstrip()
    if "push" in order :
        order=order.rsplit()
        f=funcMap[order[0]]
        f(order[1])
    else:
        f=funcMap[order]
        print(f())

