from collections import deque
N = int(input())

for i in range(N):
    M,N,K = map(int,input().split())
    board = [[0] * M for _ in range(N)]
    visit = [[False] * M for _ in range(N)]
    cnt = 0
    for j in range(K):
        X,Y = map(int,input().split())
        board[Y][X] = 1
    
    for j in range(N):
        for k in range(M):
            if(board[j][k] == 1 and not visit[j][k]):
                cnt += 1
                queue = deque([(j,k)])
                visit[j][k] = True

                while len(queue) != 0:
                    r,c = queue.popleft()
                    if r > 0 and board[r-1][c] == 1 and not visit[r-1][c]:
                        queue.append((r-1,c))
                        visit[r-1][c] = True
                    if r < N-1 and board[r+1][c] == 1 and not visit[r+1][c]:
                        queue.append((r+1,c))
                        visit[r+1][c] = True
                    if c < M-1 and board[r][c+1] == 1 and not visit[r][c+1]:
                        queue.append((r,c+1))
                        visit[r][c+1] = True
                    if c > 0 and board[r][c-1] == 1 and not visit[r][c-1]:
                        queue.append((r,c-1))
                        visit[r][c-1] = True
    print(cnt)


    