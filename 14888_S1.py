from itertools import permutations
N = int(input())
li = list(map(int,input().split()))
a,s,d,f = map(int,input().split())
arr = []

for _ in range(a):
    arr.append(1)
for _ in range(s):
    arr.append(2)
for _ in range(d):
    arr.append(3)
for _ in range(f):
    arr.append(4)

Max = -1e9
Min = 1e9
for permutation in permutations(arr,N-1):
    cnt = 0

    for i in range(N):
        if i == 0:
            cnt += li[i]
            continue

        if(permutation[i-1] == 1):
            cnt += li[i]
        if(permutation[i-1] == 2):
            cnt -= li[i]
        if(permutation[i-1] == 3):
            cnt *= li[i]
        if(permutation[i-1] == 4):
            cnt = int(cnt / li[i])
        if(permutation == (2,4,1,1,3)):
            print(cnt)
    if Max < cnt:
        print(permutation)
    Max = max(Max, cnt)
    Min = min(Min,cnt)

print(Max,Min)