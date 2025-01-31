import sys
input = sys.stdin.readline

N = int(input())

arr = []
for i in range(N):
    li = list(map(int,input().split()))
    arr.append(li)

dp = [[0] * (i+1) for i in range(N)]
dp[0] = arr[0]

Max = 0
for i in range(N-1):
    for j in range(len(arr[i])):
        dp[i+1][j] = max(dp[i+1][j],arr[i+1][j] + dp[i][j])
        dp[i+1][j+1] = max(dp[i+1][j+1],arr[i+1][j+1] + dp[i][j])

Max = max(dp[N-1])
print(Max)