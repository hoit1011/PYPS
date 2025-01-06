from collections import deque

N = int(input())
d = deque([])

for i in range(1,N+1):
    d.append(i)

for i in range(N-1):
    d.popleft()
    first = d.popleft()
    d.append(first)

print(d[0])