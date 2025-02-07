from collections import deque
N = int(input())
arr = [list(input().strip()) for _ in range(N)]

visit = [[False] * N for _ in range(N)]
cnt = 0
for i in range(N):
    for j in range(N):
        if not visit[i][j]:
            visit[i][j] = True
            n = arr[i][j]
            cnt += 1
            queue = deque([(i,j)])
            while len(queue) != 0:
                r,c = queue.popleft()
                if r > 0 and arr[r-1][c] == n and not visit[r-1][c]:
                    queue.append((r-1,c))
                    visit[r-1][c] = True
                if r < N-1 and arr[r+1][c] == n and not visit[r+1][c]:
                    queue.append((r+1,c))
                    visit[r+1][c] = True
                if c > 0 and arr[r][c-1] == n and not visit[r][c-1]:
                    queue.append((r,c-1))
                    visit[r][c-1] = True
                if c < N-1 and arr[r][c+1] == n and not visit[r][c+1]:
                    queue.append((r,c+1))
                    visit[r][c+1] = True
print(cnt, end=" ")
for i in range(N):
    for j in range(N):
        if(arr[i][j] == 'G'):
            arr[i][j] = 'R'

visit = [[False] * N for _ in range(N)]            
cnt = 0
for i in range(N):
    for j in range(N):
        if not visit[i][j]:
            visit[i][j] = True
            n = arr[i][j]
            cnt += 1
            queue = deque([(i,j)])
            while len(queue) != 0:
                r,c = queue.popleft()
                if r > 0 and arr[r-1][c] == n and not visit[r-1][c]:
                    queue.append((r-1,c))
                    visit[r-1][c] = True
                if r < N-1 and arr[r+1][c] == n and not visit[r+1][c]:
                    queue.append((r+1,c))
                    visit[r+1][c] = True
                if c > 0 and arr[r][c-1] == n and not visit[r][c-1]:
                    queue.append((r,c-1))
                    visit[r][c-1] = True
                if c < N-1 and arr[r][c+1] == n and not visit[r][c+1]:
                    queue.append((r,c+1))
                    visit[r][c+1] = True
print(cnt)