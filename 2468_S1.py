from collections import deque

N = int(input())
arr =[]
min_grd = 101
max_grd = 0

max_cnt = 0
for i in range(N):
    arr.append(list(map(int,input().split())))
    min_grd = min(min(arr[i]),min_grd)
    max_grd = max(max(arr[i]),max_grd)

for k in range(min_grd,max_grd):
    visit = [[False] * N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] > k and not visit[i][j]:
                queue = deque([(i,j)])
                cnt += 1
                while len(queue) != 0:
                    r,c = queue.popleft()
                    if r > 0 and arr[r-1][c] > k and not visit[r-1][c]:
                        queue.append((r-1,c))
                        visit[r-1][c] = True
                    if r < N-1 and arr[r+1][c] > k and not visit[r+1][c]:
                        queue.append((r+1,c))
                        visit[r+1][c] = True
                    if c > 0 and arr[r][c-1] > k and not visit[r][c-1]:
                        queue.append((r,c-1))
                        visit[r][c-1] = True
                    if c < N-1 and arr[r][c+1] > k and not visit[r][c+1]:
                        queue.append((r,c+1))
                        visit[r][c+1] = True
    max_cnt = max(cnt,max_cnt)

if(max_cnt == 0):
    print("1")
else:
    print(max_cnt)