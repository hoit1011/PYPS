import sys
input = sys.stdin.readline

# N = int(input())
# arr = []
# for _ in range(N):
#     n = list(map(int,input().split()))    
#     arr.append(n)

# arr.sort()

# Max = 0
# for i in range(N):
#     Start = arr[i][1]
#     cnt = 1
#     for j in range(N):
#         if(arr[j][0] >= Start):
#             cnt += 1
#             Start = arr[j][1]
#     if(Max < cnt):
#         Max = cnt

# print(Max)

N = int(input())
arr = []

for _ in range(N):
    n = list(map(int,input().split()))    
    arr.append(n)

arr.sort(key=lambda x : (x[1], x[0]))

start = arr[0][1]
cnt = 1

for i in range(1,N):
    if(start <= arr[i][0]):
        cnt += 1
        start = arr[i][1]

print(cnt)