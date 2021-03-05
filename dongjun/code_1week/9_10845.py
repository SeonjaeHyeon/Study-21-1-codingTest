class CustomQueue:
    def __init__(self):
        self.value = []
        self.cnt = 0

    def push(self, X):
        self.value.append(X)
        self.cnt += 1

    def pop(self):
        if self.empty() == 1:
            return -1
        data = self.value[0]
        del self.value[0]
        self.cnt -= 1
        return data

    def size(self):
        return self.cnt

    def empty(self):
        return 1 if self.cnt == 0 else 0

    def front(self):
        if self.empty() == 1:
            return -1
        return self.value[0]

    def back(self):
        if self.empty() == 1:
            return -1
        return self.value[-1]


N = int(input())
queue = CustomQueue()
for _ in range(N):
    arr = input().split()
    order = arr[0]
    if order == "push":
        queue.push(arr[1])
    elif order == "pop":
        print(queue.pop())
    elif order == "size":
        print(queue.size())
    elif order == "empty":
        print(queue.empty())
    elif order == "front":
        print(queue.front())
    elif order == "back":
        print(queue.back())
