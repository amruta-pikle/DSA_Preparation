class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return "stack is empty"

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return "stack is empty"

    def size(self):
        return len(self.stack)

s = Stack()
s.push(10)
s.push(20)
print(s.peek())  # 20
print(s.pop())   # 20
print(s.size())  # 1