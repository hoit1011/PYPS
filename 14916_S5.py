N = int(input())
dp = [0] * (N + 4)
dp[0] = -1
dp[1] = 1
dp[2] = -1
dp[3] = 2
dp[4] = 1
for i in range(5,N):
    if dp[i-2] == -1 and dp[i-5] == -1:
        dp[i] = -1
    elif dp[i-2] == -1:
        dp[i] = dp[i-5] + 1
    elif dp[i-5] == -1:
        dp[i] = dp[i-2] + 1
    else:
        dp[i] = min(1+dp[i-2], 1+dp[i-5])
print(dp[N-1])
        