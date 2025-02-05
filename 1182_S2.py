from itertools import combinations

N,S = map(int,input().split())
li = list(map(int,input().split()))

cnt = 0
for i in range(1,N+1):
    for combination in combinations(li,i):
        if sum(combination) == S:
            cnt += 1

print(cnt)