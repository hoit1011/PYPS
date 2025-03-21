from itertools import permutations

N, K = map(int,input().split())
li = list(map(int,input().split()))

res = 0

for permutation in permutations(li,N):
    cnt = 500
    check = True

    for i in range(N):
        cnt -= K
        cnt += int(permutation[i])
        
        if cnt < 500:
            check = False
            break

    if check:
        res += 1

print(res)