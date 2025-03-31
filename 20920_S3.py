N, M = map(int,input().split())

d = {}
for i in range(N):
    S = input().strip()
    if len(S) >= M:
        if S not in d:
            d[S] = 0
        d[S] += 1

arr = sorted(d.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

for i in arr:
    print(i[0])