N = int(input())

arr = []
for _ in range(N):
    T , P = map(int,input().split())
    arr.append((T,P))

Max = 0

dp = [0] * (N + 1)

for i in range(N):
    n = arr[i][0] + i 
    for j in range(i,N+1):
        if j >= n:
            dp[j] = max(dp[i] + arr[i][1],dp[j])

print(dp[N])
        
