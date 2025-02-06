import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
arr = []

for i in range(N):
    arr.append(input())

visit = [[False] * N for _ in range(N)]

cntarr = []
for i in range(N):
    for j in range(N):
        if(arr[i][j] == '1' and not visit[i][j]):
            cnt = 1
            visit[i][j] = True
            queue = deque([(i,j)])
            while len(queue) != 0:
                r,c = queue.popleft()
                if r > 0 and arr[r-1][c] == '1' and not visit[r-1][c]:
                    queue.append((r-1,c))
                    visit[r-1][c] = True
                    cnt += 1
                if r < N-1 and arr[r+1][c] == '1' and not visit[r+1][c]:
                    queue.append((r+1,c))
                    visit[r+1][c] = True
                    cnt += 1
                if c < N-1 and arr[r][c+1] == '1' and not visit[r][c+1]:
                    queue.append((r,c+1))
                    visit[r][c+1] = True
                    cnt += 1
                if c > 0 and arr[r][c-1] == '1' and not visit[r][c-1]:
                    queue.append((r,c-1))
                    visit[r][c-1] = True
                    cnt += 1
            cntarr.append(cnt)
cntarr.sort()
print(len(cntarr))
for i in range(len(cntarr)):
    print(cntarr[i])