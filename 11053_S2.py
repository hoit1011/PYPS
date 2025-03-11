N = int(input())
numbers = list(map(int,input().split()))
arr = []
for i in range(N):
    s = numbers[i]
    cnt = 0
    for j in range(i,N):
        if s < numbers[j]:
            cnt += 1
            s = numbers[j]
    arr.append(cnt)
print(max(arr)+1)