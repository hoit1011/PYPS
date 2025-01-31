N = int(input())

arr = []
for i in range(N):
    r,g,b = map(int,input().split())
    arr.append((r,g,b))

R = [0]*N
G = [0]*N
B = [0]*N

R[0] = arr[0][0]
G[0] = arr[0][1]
B[0] = arr[0][2]

for i in range(1,N):
    R[i] = arr[i][0] + min(G[i-1],B[i-1])
    G[i] = arr[i][1] + min(R[i-1],B[i-1])
    B[i] = arr[i][2] + min(R[i-1],G[i-1])

print(min(R[N-1],G[N-1],B[N-1]))