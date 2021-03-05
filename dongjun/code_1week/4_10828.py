class CustomStack:
    def __init__(self):
        self.value = []
        self.cnt = 0

    def push(self, X):
        self.value.append(X)
        self.cnt += 1

    def pop(self):
        if self.empty() == 1:
            return -1
        data = self.value[-1]
        del self.value[-1]
        self.cnt -= 1
        return data

    def size(self):
        return self.cnt

    def empty(self):
        return 1 if self.cnt == 0 else 0

    def top(self):
        if self.empty() == 1:
            return -1
        return self.value[-1]


N = int(input())
stack = CustomStack()
for _ in range(N):
    arr = input().split()
    order = arr[0]
    if order == "push":
        stack.push(arr[1])
    elif order == "pop":
        print(stack.pop())
    elif order == "size":
        print(stack.size())
    elif order == "empty":
        print(stack.empty())
    elif order == "top":
        print(stack.top())
