from collections import deque

N, M = map(int,input().split())
arr = []
for _ in range(N):
    arr.append(input())

visit = [[False] * M for _ in range(N)]
dist = [[False] * M for _ in range(N)]
queue = deque([(0,0)])
visit[0][0] = True
dist[0][0] = 0

while len(queue) != 0:
    r,c = queue.popleft()
    if r > 0 and arr[r-1][c] == '1' and not visit[r-1][c]:
        queue.append((r-1,c))
        visit[r-1][c] = True
        dist[r-1][c] = dist[r][c] + 1
    if r < N-1 and arr[r+1][c] == '1' and not visit[r+1][c]:
        queue.append((r+1,c))
        visit[r+1][c] = True
        dist[r+1][c] = dist[r][c] + 1
    if c < M - 1 and arr[r][c+1] == '1' and not visit[r][c+1]:
        queue.append((r,c+1))
        visit[r][c+1] = True
        dist[r][c+1] = dist[r][c] + 1
    if c > 0 and arr[r][c-1] == '1' and not visit[r][c-1]:
        queue.append((r,c-1))
        visit[r][c-1] = True
        dist[r][c-1] = dist[r][c] + 1

print(dist[N-1][M-1] + 1)