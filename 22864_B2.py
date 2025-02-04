A,B,C,M = map(int,input().split())

cnt = 0
pi = 0
for i in range(24):
    if (pi + A) <= M:
        pi += A
        cnt += B
    else:
        pi -= C
        if pi < 0:
            pi = 0

print(cnt)