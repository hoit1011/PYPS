A = str(input())

N = int(input())
cnt = 0

for i in range(N):
    Str = str(input())
    if A[:5] == Str[:5]:
        cnt += 1

print(cnt)