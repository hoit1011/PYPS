N = int(input())
dp = [0] * N
dp[0] = 1

if N >= 2:
    dp[1] = 1
    for i in range(2,N):
        dp[i] = dp[i-1]+ dp[i-2]
    print(dp[N-1])
else:
    print(dp[N-1])