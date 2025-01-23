N,K = map(int,input().split())

arr = []
for i in range(N):
    num = int(input())
    arr.append(num)

arr.sort(reverse=True)

cnt = 0
for i in range(N):
    if K // arr[i] != 0:
        n = K // arr[i]
        cnt += n
        K -= arr[i] * n

print(cnt)