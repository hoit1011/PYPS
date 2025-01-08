import sys
input = sys.stdin.readline

N = int(input())

for _ in range(N):
    n = int(input())
    arr = []

    for i in range(n):
        a,b = list(map(int,input().split()))
        arr.append((a,b))

    arr.sort()

    Max = 1e9
    cnt = 0
    for i in range(n):
        if(arr[i][1] <= Max):
            cnt += 1
            Max = arr[i][1]
    
    print(cnt)
