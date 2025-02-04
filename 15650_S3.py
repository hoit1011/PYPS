def dfs(start):
    if(len(path) == M):
        print(' '.join(map(str,path)))
        return
    for i in range(start, N + 1):
        path.append(i)
        dfs(i + 1)
        path.pop()

N,M = map(int,input().split())
path = []

dfs(1)
    