N = int(input())
km = list(map(int,input().split()))
money = list(map(int,input().split()))

cnt = 0
Min = 1e9
for i in range(N-1):
    Min = min(money[i],Min)
    cnt += km[i] * Min

print(cnt)

