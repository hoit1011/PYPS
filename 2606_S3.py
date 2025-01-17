N = int(input())
M = int(input())

adj = [[] for _ in range(N)]

for i in range(M):
    u,v = map(int,input().split())
    adj[u-1].append(v-1)
    adj[v-1].append(u-1)

visit = [False] * N

def dfs(u):
    visit[u] = True

    for v in adj[u]:
        if not visit[v]:
            dfs(v)

count = 0
dfs(0)
for i in range(1,N):
    if visit[i]:
        count += 1

print(count)