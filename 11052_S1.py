N = int(input())
li = list(map(int,input().split()))
dp = [0] * (N + 1)

for i in range(1,N+1):
    for j in range(1,i+1):
        dp[i] = max(dp[i], li[j-1] + dp[i-j])

print(dp[N])
