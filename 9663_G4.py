import sys
input = sys.stdin.readline

n = int(input())
ans = 0
visit = [-1] * n

def check(now_row):
    for row in range(now_row):
        if visit[now_row] == visit[row] or now_row - row == abs(visit[now_row] - visit[row]):
            return False
        
    return True

def dfs(row):
    global ans

    if row == n:
        ans += 1

    else:
        for i in range(n):
            visit[row] = i
            if check(row):
                dfs(row + 1)

dfs(0)
print(ans)