N = int(input())
li = list(map(int,input().split()))

li.reverse()
arr = []
cnt = N
for i in range(N):
    arr.insert(li[i],cnt)
    cnt -= 1

for i in range(N):
    print(arr[i],end=" ")