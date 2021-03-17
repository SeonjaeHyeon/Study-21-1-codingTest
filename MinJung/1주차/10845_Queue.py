import sys 

queue = [] 
def push(X):
    queue.append(X)
def pop():
    if queue == []:
        return -1
    queue.reverse()
    p=queue.pop()
    queue.reverse()
    return p
def size():
    return len(queue)
def empty():
    if queue==[]:
        return 1
    else:
        return 0
def front():
    if queue==[]:
        return -1
    return queue[0]
def back():
    if queue ==[]:
        return(-1)
    return int(queue[len(queue)-1])

funcMap ={
    "push":push,
    "pop":pop,
    "size":size,
    "empty":empty,
    "front":front,
    "back":back
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

