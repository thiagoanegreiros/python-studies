class MyStack:

    stack: list

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        return self.stack.pop()

    def top(self) -> int:
        print('----')
        print(self.stack)
        print('----')
        return self.stack[-1]

    def empty(self) -> bool:
        return len(self.stack) == 0

s = MyStack()
s.push(10)
s.push(20)
s.push(30)

print(s.top())    # 30
print(s.pop())    # 30
print(s.top())    # 20
print(s.empty())  # False
