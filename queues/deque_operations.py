from collections import deque

queue = deque()

queue.append(19)
queue.append(20)
queue.append(44)
queue.append(654)
queue.append(87)
queue.append(9987)

queue.pop()
queue.popleft()


queue.rotate()


queue.extend([1,2])


queue.append([8,55])

queue.appendleft(-4)

queue.extendleft([-98])


print(list(queue))