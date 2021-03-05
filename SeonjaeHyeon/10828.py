import sys

n = int(input())

stack = []

def push(n):
    stack.append(n)

def pop():
    return stack.pop() if stack else -1

def size():
    return len(stack)

def empty():
    return 0 if stack else 1

def top():
    return stack[-1] if stack else -1

cmd = {
    'pop': pop,
    'size': size,
    'empty': empty,
    'top': top,
}

for _ in range(n):
    args = sys.stdin.readline().rstrip()

    if args.startswith('push'):
        push(args[5:])
        continue

    print(cmd[args]())
