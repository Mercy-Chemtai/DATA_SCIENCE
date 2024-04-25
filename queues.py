#implementation of queues as a list
#initialization of a queue
queue=[]

#adding elements to a queue
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
print(queue)

#removing Items in queue
queue.pop(3)
print(queue)


#implementation of queues as deque  
from collections import deque
#initializing deque
q = deque()
#pushing elements to a queue
q.append(1)
q.append(2)
q.append(3)
q.append(4)
print(q)
#removing item in a queue
q.popleft()
q.popleft()
print(q)

 #implementation of queue.Queue
from queue import Queue
t=Queue(maxsize=4)
print(t.qsize())
# adding elements
t.put(1)
t.put(2)
t.put(3)
t.put(4)

print(t.full())
print(t.empty())
#removing elements
print(t.get(1))
print(t.qsize())