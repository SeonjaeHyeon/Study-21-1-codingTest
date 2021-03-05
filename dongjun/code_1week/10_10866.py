class CustomDeque:
    def __init__(self):
        self.value = []
        self.cnt = 0

    def push_front(self, X):
        self.value.insert(0, X)
        self.cnt += 1

    def push_back(self, X):
        self.value.append(X)
        self.cnt += 1

    def pop_front(self):
        if self.empty() == 1:
            return -1
        data = self.value[0]
        del self.value[0]
        self.cnt -= 1
        return data

    def pop_back(self):
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

    def front(self):
        if self.empty() == 1:
            return -1
        return self.value[0]

    def back(self):
        if self.empty() == 1:
            return -1
        return self.value[-1]


N = int(input())
deque = CustomDeque()
for _ in range(N):
    arr = input().split()
    order = arr[0]
    if order == "push_front":
        deque.push_front(arr[1])
    elif order == "push_back":
        deque.push_back(arr[1])
    elif order == "pop_front":
        print(deque.pop_front())
    elif order == "pop_back":
        print(deque.pop_back())
    elif order == "size":
        print(deque.size())
    elif order == "empty":
        print(deque.empty())
    elif order == "front":
        print(deque.front())
    elif order == "back":
        print(deque.back())
