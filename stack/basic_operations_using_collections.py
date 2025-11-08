from collections import deque

stack = deque(maxlen=3)

stack.append(45)
stack.append(50)
stack.append(84)
stack.append(786)
stack.appendleft(56)

# stack.pop()


print(list(stack))