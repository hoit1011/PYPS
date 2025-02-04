import sys
input = sys.stdin.readline

N,K = map(int,input().split())

arr = []
for i in range(N):
    a,b = map(int,input().split())
    arr.append((b,a))

dp = [0] * (K + 1) 

for cost,weight in arr:
    for j in range(K, weight - 1, -1):
        dp[j] = max(dp[j],dp[j-weight]+cost)
    
print(dp[K])




# for i in range(N):
#     cost = arr[i][0]
#     Weight = arr[i][1]
#     for j in range(i,N):
#         if i == j:
#             continue
#         if K >= Weight + arr[j][1]:
#             Weight += arr[j][1]
#             cost += arr[j][0]
#     dp.append(cost)

# print(max(dp))