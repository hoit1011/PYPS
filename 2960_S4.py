N,K = map(int,input().split())
arr = []
for i in range(2,N+1):
    arr.append(i)

cnt = 0
while True:
    Min = min(arr)
    de = []
    for i in range(len(arr)):
        if(arr[i] % Min == 0):
            cnt += 1
        else:
            de.append(arr[i])

        if(cnt == K):
            print(arr[i])
            exit()
    arr = de

