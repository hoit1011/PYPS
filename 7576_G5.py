import sys
input = sys.stdin.readline

from collections import deque

N, M = map(int,input().split())
arr = []
for i in range(M):
    arr.append(list(map(int,input().split())))

dist =[[-1] * N for _ in range(M)]
queue = deque([])
for i in range(M):
    for j in range(N):
        if(arr[i][j] == 1):
            queue.append((i,j))
            dist[i][j] = 0
            
while len(queue) != 0:
    r,c = queue.popleft()
    if r > 0 and arr[r-1][c] == 0 and dist[r-1][c] == -1:
        dist[r-1][c] = dist[r][c] + 1
        queue.append((r-1, c))

    if r < M-1 and arr[r+1][c] == 0 and dist[r+1][c] == -1:
        dist[r+1][c] = dist[r][c] + 1
        queue.append((r+1, c))

    # 좌
    if c > 0 and arr[r][c-1] == 0 and dist[r][c-1] == -1:
        dist[r][c-1] = dist[r][c] + 1
        queue.append((r, c-1))

    # 우
    if c < N-1 and arr[r][c+1] == 0 and dist[r][c+1] == -1:
        dist[r][c+1] = dist[r][c] + 1
        queue.append((r, c+1))

Max = 0
for i in range(M):
    for j in range(N):
        if(arr[i][j] == 0 and dist[i][j] == -1):
            print("-1")
            exit()
        Max = max(dist[i][j],Max)
print(Max)