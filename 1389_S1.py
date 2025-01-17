import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().split())
adj = [[] for _ in range(N)]

for i in range(M):
    A,B = map(int,input().split())
    adj[A-1].append(B-1)
    adj[B-1].append(A-1)

abcd = 0
Max = 1e9
for i in range(N):
    visit = [-1] * N
    visit[i] = 0
    
    queue = deque([i])
    while queue:
        node =  queue.popleft()
        for k in adj[node]:
            if visit[k] == -1:
                visit[k] = visit[node] + 1
                queue.append(k)

    cnt = 0
    for j in range(len(visit)):
        cnt += visit[j]
    
    if(cnt < Max):
        Max = cnt
        abcd = i

print(abcd + 1)

