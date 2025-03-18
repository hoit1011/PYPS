from collections import deque

n,m = map(int,input().split())

li = []

for i in range(n):
    li.append(list(input().split()))

dist = [[-1 for _ in range(m)] for _ in range(n)]

queue = deque([])
for i in range(n):
    for j in range(m):
        if li[i][j] == '2':
            queue.append((i,j))
            dist[i][j] = 0

while(len(queue) != 0):
    r,c = queue.popleft()
    if r > 0 and dist[r-1][c] == -1 and li[r-1][c] == '1':
        queue.append((r-1,c))
        dist[r-1][c] = dist[r][c] + 1
    if r < n-1 and dist[r+1][c] == -1 and li[r+1][c] == '1':
        queue.append((r+1,c))
        dist[r+1][c] = dist[r][c] + 1
    if c > 0 and dist[r][c-1] == -1 and li[r][c-1] == '1':
        queue.append((r,c-1))
        dist[r][c-1] = dist[r][c] + 1
    if c < m-1 and dist[r][c+1] == -1 and li[r][c+1] == '1':
        queue.append((r,c+1))
        dist[r][c+1] = dist[r][c] + 1

for i in range(len(dist)):
    for j in range(len(dist[i])):
        if li[i][j] == '0' and dist[i][j] == -1:
            print("0",end=' ')
        elif li[i][j] == '1' and dist[i][j] == -1:
            print("-1",end=' ')
        else:
            print(dist[i][j],end=' ')
    print()