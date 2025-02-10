from itertools import combinations

N,K = map(int,input().split())
li = list(map(int,input().split()))

cnt = 0
for i in range(2,N):
    for combination in combinations(li,i):
        if sum(combination) == K:
            print(combination)
            cnt += 1

print(cnt)

