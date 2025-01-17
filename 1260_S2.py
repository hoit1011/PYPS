import sys
input = sys.stdin.readline
from collections import deque

N,M,V = map(int,input().split())

adj = [[] for _ in range(N + 1)]


for i in range(M):
    u,v = map(int,input().split())
    adj[u].append(v)
    adj[v].append(u)

for i in range(1, N+1):
    adj[i].sort()

visit = [False] * (N + 1)
arr = []

def dfs(st):
    visit[st] = True
    arr.append(st)
    for i in adj[st]:
        if not visit[i]:
            visit[i] = True
            dfs(i)

dfs(V)
for i in range(len(arr)):
    print(arr[i],end=" ")

visit = [False] * (N + 1)
arr = []

queue = deque([V])

while queue:
    node = queue.popleft()
    visit[node] = True
    arr.append(node)
    for i in adj[node]:
        if not visit[i]:
            visit[i] = True
            queue.append(i)

print("")
for i in range(len(arr)):
    print(arr[i],end=" ")