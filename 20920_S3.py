N, M = map(int,input().split())

d = {}
for i in range(N):
    S = input()
    if len(S) >= M:
        if S not in d:
            d[S] = 0
        d[S] += 1

