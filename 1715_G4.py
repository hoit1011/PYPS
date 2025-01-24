import heapq

N = int(input())
arr = []
for _ in range(N):
    heapq.heappush(arr,int(input()))

cnt = 0

while len(arr) > 1:
    cost1 = heapq.heappop(arr)
    cost2 = heapq.heappop(arr)
    result = cost1 + cost2
    heapq.heappush(arr,result)
    cnt += result

print(cnt)