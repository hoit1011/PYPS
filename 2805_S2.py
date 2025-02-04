N,M = map(int,input().split())
li = list(map(int,input().split()))

low = 0
high = max(li)
answer = -1
while low <= high:
    mid = (low + high) // 2

    total = 0
    for i in range(N):
        if li[i] > mid:
            total += li[i] - mid
    
    if total >= M:
        answer = mid
        low = mid + 1
    else:
        high = mid -1
    
print(answer)