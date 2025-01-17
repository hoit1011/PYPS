import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())

adj =[[] for _ in range(N)]
for i in range(N-1):
    u,v = map(int,input().split())
    adj[u-1].append(v-1)
    adj[v-1].append(u-1)
visit = [False] * N
arr = [-1] * N

def dfs(st):
    visit[st] = True
    for i in adj[st]:
        if not visit[i]:
            arr[i] = st
            dfs(i)

dfs(0)

for i in range(1,N):
    print(arr[i]+1)
