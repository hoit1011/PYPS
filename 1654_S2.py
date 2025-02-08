K , N = map(int,input().split())
arr = []
for i in range(K):
    arr.append(int(input()))

left = 1
right = max(arr)
answer = 0
while left <= right:
    mid = (left + right) // 2 
    cnt = 0

    for i in range(K):
        cnt += arr[i] // mid

    
    if cnt >= N:
        left = mid + 1
        answer = mid
    else:
        right = mid - 1

print(answer)