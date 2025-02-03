N = int(input())

for i in range(N):
    n = int(input())

    if n == 1:
        print("1")
    elif n == 2:
        print("1")
    elif n == 3:
        print("1")
    else:
        dp = [0] * n
        dp[0] = 1
        dp[1] = 1
        dp[2] = 1
        for j in range(3,n):
            dp[j] = dp[j-2] + dp[j-3]
        print(dp[n-1])
