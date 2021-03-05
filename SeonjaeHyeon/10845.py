import sys

n = int(input())

queue = []

def push(n):
    queue.append(n)

def pop():
    return queue.pop(0) if queue else -1

def size():
    return len(queue)

def empty():
    return 0 if queue else 1

def front():
    return queue[0] if queue else -1

def back():
    return queue[-1] if queue else -1

cmd = {
    'pop': pop,
    'size': size,
    'empty': empty,
    'front': front,
    'back': back,
}

for _ in range(n):
    args = sys.stdin.readline().rstrip()

    if args.startswith('push'):
        push(args[5:])
        continue

    print(cmd[args]())
