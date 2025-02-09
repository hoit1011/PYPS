from itertools import combinations

N = int(input())
arr = []
for i in range(N):
    n = list(map(int,input().split()))
    arr.append(n)

Mincnt = 1e9
for combination in combinations(list(range(N)), N // 2):
    notpick = []
    for i in range(N):
        if i not in combination:
            notpick.append(i)
    Start = 0
    Link = 0
    for i in combination:
        for j in combination:
            if i == j:
                continue
            Start += arr[i][j]
    
    for i in notpick:
        for j in notpick:
            if i == j:
                continue
            Link += arr[i][j]
    
    Mincnt = min(abs(Start-Link),Mincnt)
    
print(Mincnt)