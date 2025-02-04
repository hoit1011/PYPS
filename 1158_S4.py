from collections import deque

N, K = map(int,input().split())
arr = deque([])

for i in range(1,N+1):
    arr.append(i)

print("<",end='')
cnt = 1
n = 0
while True:
    if len(arr) == 0:
        break

    if cnt != K:
        arr.append(arr.popleft())
        cnt += 1
    else:
        cnt = 1
        n += 1
        print(arr.popleft(),end="")
        if(n != N):
            print(", ",end="")

print(">")
