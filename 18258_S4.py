import sys
from collections import deque

n = int(input())

queue = deque([])

for i in range(n):
    li = sys.stdin.readline()
    li = li.split()
    first = li[0]
    if(first == "push"):
        queue.append(li[1])
    
    if(first == "pop"):
        if(len(queue) == 0):
            print("-1")
        else:
            print(queue.popleft())
    
    if(first == "size"):
        print(len(queue))
    
    if(first == "empty"):
        if(len(queue) == 0):
            print("1")
        else:
            print("0")
    
    if(first == "front"):
        if(len(queue) == 0):
            print("-1")
        else:
            print(queue[0])
    if(first == "back"):
        if(len(queue) == 0):
            print("-1")
        else:
            print(queue[-1])