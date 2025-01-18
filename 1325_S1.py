import sys
input = sys.stdin.readline
from collections import deque 

N,M = map(int,input().split())

parents = [[] for _ in range(N)]

for i in range(M):
    u,v = map(int,input().split())
    parents[v - 1].append(u - 1)

Maxcnt = 0
arr = []
for i in range(N):
    visit = [False] * N
    visit[i] = True
    cnt = 1

    queue = deque([i])
    while queue:
        node = queue.popleft()
        for i in parents[node]:
            if not visit[i]:
                visit[i] = True
                queue.append(i)
                cnt += 1

    if cnt > Maxcnt:
        Maxcnt = cnt

    arr.append(cnt)

for i in range(len(arr)):
    if arr[i] == Maxcnt:
        print(i+1,end=" ")