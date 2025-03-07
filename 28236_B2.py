n,m,k = map(int,input().split())
arr = []
for i in range(k):
    a,b = map(int,input().split())
    arr.append((a,b))
li = [0] * k
for i in range(k):
    li[i] += arr[i][0] - 1
    li[i] += n - arr[i][1]
Min = min(li)
for i in range(k):
    if li[i] == Min:
        print(i+1)
        exit()