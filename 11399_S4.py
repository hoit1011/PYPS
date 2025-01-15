N = int(input())

li = list(map(int,input().split()))


li.sort(reverse=True)

cnt = 0

for i in range(N):
    cnt += li[i] * (i + 1)


print(cnt)