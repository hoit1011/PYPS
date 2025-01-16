N = int(input())
parrent = list(map(int,input().split()))
R = int(input())

root = 0
for i in range(N):
    if parrent[i] == -1:
        root = i
        break

black = [0] * N
for i in range(N):
    u = i
    while True:
        if u == R:
            black[i] = 1
            break
        if u == root:
            break
        u = parrent[u]

red = [0] * N
for i in range(N):
    if black[i] == 1:
        continue
    
    if i == root:
        continue

    red[parrent[i]] = 1

count = 0
for i in range(N):
    if black[i] == 1 or red[i] == 1:
        continue
    count +=1

print(count)
