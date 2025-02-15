from itertools import combinations
from collections import deque
N, M = map(int,input().split())

arr = []
for _ in range(N):
    arr.append(list(map(int,input().split())))
two_arr = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            two_arr.append((i,j))

Min = 1e9
for combination in combinations(two_arr,M):
    queue = deque(combination)
    visit = [[False] * N for _ in range(N)]
    dist = [[-1] * N for _ in range(N)]
    for i,j in combination:
        visit[i][j] = True
        dist[i][j] = 0
    while len(queue) != 0:
        r,c = queue.popleft()
        if r > 0 and not visit[r-1][c]:
            queue.append((r-1,c))
            visit[r-1][c] = True
            dist[r-1][c] = dist[r][c] + 1
        if r < N - 1 and not visit[r+1][c]:
            queue.append((r+1,c))
            visit[r+1][c] = True
            dist[r+1][c] = dist[r][c] + 1
        if c > 0 and not visit[r][c-1]:
            queue.append((r,c-1))
            visit[r][c-1] = True
            dist[r][c-1] = dist[r][c] + 1
        if c < N - 1 and not visit[r][c+1]:
            queue.append((r,c+1))
            visit[r][c+1] = True
            dist[r][c+1] = dist[r][c] + 1

    Sum = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                Sum += dist[i][j]
    Min = min(Min,Sum)

print(Min)
