from itertools import combinations
from collections import deque
N,M = map(int, input().split())

arr = []
for i in range(N):
    li = list(map(int,input().split()))
    arr.append(li)

biras = []
xy = []
for i in range(N):
    for j in range(M):
        if(arr[i][j] == 0):
            xy.append((i,j))
        if(arr[i][j] == 2):
            biras.append((i,j))
Max = 0
for combination in combinations(xy,3):
    arrs = arr
    visit = [[False] * M for _ in range(N)]
    queue = deque(biras)
    cnt = 0
    for j in combination:
        arrs[j[0]][j[1]] = 1
    while len(queue) != 0:
        r,c = queue.popleft()
        if r > 0 and arrs[r-1][c] == 0 and not visit[r-1][c]:
            queue.append((r-1,c))
            visit[r-1][c] = True
        if r < N - 1 and arrs[r+1][c] == 0 and not visit[r+1][c]:
            queue.append((r+1,c))
            visit[r+1][c] = True
        if c > 0 and arrs[r][c-1] == 0 and not visit[r][c-1]:
            queue.append((r,c-1))
            visit[r][c-1] = True
        if c < M - 1 and arrs[r][c+1] == 0 and not visit[r][c+1]:
            queue.append((r,c+1))
            visit[r][c+1] = True

    for i in range(N):
        for j in range(M):
            if visit[i][j] == False and arrs[i][j] == 0:
                cnt += 1
    Max = max(Max,cnt)
    for j in combination:
        arrs[j[0]][j[1]] = 0

print(Max)