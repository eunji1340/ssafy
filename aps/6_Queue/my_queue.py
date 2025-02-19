queue = [0] * 3
front = rear = -1

rear += 1  # euqueue 1
queue[rear] = 1

rear += 1  # enqueue 2
queue[rear] = 2

rear += 1  # enqueue 3
queue[rear] = 3

while front != rear:  # 큐에 원소가 남아있으면
    front += 1  # dequeue
    t = queue[front]
    print(t)
print(queue)

