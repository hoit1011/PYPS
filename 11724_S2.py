import sys
from collections import deque
input = sys.stdin.readline
N,M = map(int,input().split())
adj = [[] for _ in range(N)]

for i in range(M):
    u,v = map(int,input().split())
    adj[u - 1].append(v - 1)
    adj[v - 1].append(u - 1)

visit = [False] * N
count = 0

for i in range(N):
    if visit[i]:
        continue

    count += 1

    queue = deque([i])
    while queue:
        node = queue.popleft()
        for j in adj[node]:
            if not visit[j]:
                visit[j] = True
                queue.append(j)

print(count)