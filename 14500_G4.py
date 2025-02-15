N,M = map(int,input().split())

board = [list(map(int,input().split())) for _ in range(N)]

tetromino = [
    [(0, 0), (0, 1), (1, 0), (1, 1)],
    [(0, 0), (0, 1), (0, 2), (0, 3)], 
    [(0, 0), (1, 0), (2, 0), (3, 0)], 
    [(0, 0), (0, 1), (0, 2), (1, 0)],
    [(1, 0), (1, 1), (1, 2), (0, 2)],
    [(0, 0), (1, 0), (1, 1), (1, 2)], 
    [(0, 0), (0, 1), (0, 2), (1, 2)], 
    [(0, 0), (1, 0), (2, 0), (2, 1)],
    [(2, 0), (2, 1), (1, 1), (0, 1)],
    [(0, 0), (0, 1), (1, 0), (2, 0)],
    [(0, 0), (0, 1), (1, 1), (2, 1)],
    [(0, 0), (0, 1), (0, 2), (1, 1)],  
    [(1, 0), (1, 1), (1, 2), (0, 1)], 
    [(0, 0), (1, 0), (2, 0), (1, 1)],  
    [(1, 0), (0, 1), (1, 1), (2, 1)],  
    [(1, 0), (2, 0), (0, 1), (1, 1)],
    [(0, 0), (1, 0), (1, 1), (2, 1)],
    [(1, 0), (0, 1), (1, 1), (0, 2)],
    [(0, 0), (0, 1), (1, 1), (1, 2)]
]

answer = 0
def find(x,y):
    global answer

    for i in range(len(tetromino)):
        result = 0
        for j in range(4):
            try:
                next_x = x + tetromino[i][j][0]
                next_y = y + tetromino[i][j][1]
                result += board[next_x][next_y]
            except IndexError:
                break
        answer = max(answer,result)

for i in range(N):
    for j in range(M):
        find(i,j)

print(answer)