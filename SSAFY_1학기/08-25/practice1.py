que = [[] for _ in range(3)]
front = -1
rear = -1

def enque(x):
    global rear
    rear += 1
    que[rear] = x

def deque():
    global front
    front += 1
    return que[front]

enque(1)
enque(2)
enque(3)
print(deque())
print(deque())
print(deque())
