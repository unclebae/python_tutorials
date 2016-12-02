from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")
queue.append("Graham")

print(queue)
print("Pop Left : ", queue.popleft())
print("Pop Left : ", queue.popleft())

print(queue)